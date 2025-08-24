import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Optional
import warnings
warnings.filterwarnings('ignore')

class ResidualQuantizer(nn.Module):
    """
    Residual Quantizer module for RQ VAE
    
    This module implements hierarchical residual quantization where
    each layer quantizes the residual from the previous layer.
    """
    
    def __init__(self, input_dim: int, n_embeddings: int = 512, 
                 embedding_dim: int = 64, commitment_cost: float = 0.25):
        """
        Initialize Residual Quantizer
        
        Args:
            input_dim: Dimension of input vectors
            n_embeddings: Number of embeddings in codebook
            embedding_dim: Dimension of each embedding
            commitment_cost: Commitment loss weight
        """
        super().__init__()
        self.input_dim = input_dim
        self.n_embeddings = n_embeddings
        self.embedding_dim = embedding_dim
        self.commitment_cost = commitment_cost
        
        # Initialize embedding table
        self.embedding = nn.Embedding(n_embeddings, embedding_dim)
        self.embedding.weight.data.uniform_(-1.0 / n_embeddings, 1.0 / n_embeddings)
        
        # Projection layers for input and output
        self.input_proj = nn.Linear(input_dim, embedding_dim)
        self.output_proj = nn.Linear(embedding_dim, input_dim)
        
    def forward(self, inputs: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Forward pass through residual quantizer
        
        Args:
            inputs: Input tensor of shape (batch_size, input_dim)
            
        Returns:
            quantized: Quantized output
            loss: Quantization loss
            perplexity: Codebook usage statistics
        """
        batch_size = inputs.size(0)
        
        # Project input to embedding space
        flat_input = inputs.view(-1, self.input_dim)
        flat_input = self.input_proj(flat_input)
        
        # Calculate distances to embeddings
        distances = (torch.sum(flat_input**2, dim=1, keepdim=True) 
                    + torch.sum(self.embedding.weight**2, dim=1)
                    - 2 * torch.matmul(flat_input, self.embedding.weight.t()))
        
        # Find nearest embeddings
        encoding_indices = torch.argmin(distances, dim=1).unsqueeze(1)
        encodings = torch.zeros(encoding_indices.shape[0], self.n_embeddings, device=inputs.device)
        encodings.scatter_(1, encoding_indices, 1)
        
        # Quantize and unflatten
        quantized = torch.matmul(encodings, self.embedding.weight)
        quantized = self.output_proj(quantized)
        quantized = quantized.view(batch_size, self.input_dim)
        
        # Calculate losses
        e_latent_loss = F.mse_loss(quantized.detach(), inputs)
        q_latent_loss = F.mse_loss(quantized, inputs.detach())
        loss = q_latent_loss + self.commitment_cost * e_latent_loss
        
        # Straight-through estimator
        quantized = inputs + (quantized - inputs).detach()
        
        # Calculate perplexity
        avg_probs = torch.mean(encodings, dim=0)
        perplexity = torch.exp(-torch.sum(avg_probs * torch.log(avg_probs + 1e-10)))
        
        return quantized, loss, perplexity


class RQVAE(nn.Module):
    """
    Residual Quantized Variational Autoencoder
    
    This VAE uses residual quantization to improve encoding quality
    and reduce posterior collapse issues.
    """
    
    def __init__(self, input_dim: int, hidden_dim: int = 128, 
                 latent_dim: int = 32, n_layers: int = 3,
                 n_embeddings: int = 512, embedding_dim: int = 64):
        """
        Initialize RQ VAE
        
        Args:
            input_dim: Dimension of input data
            hidden_dim: Dimension of hidden layers
            latent_dim: Dimension of latent space
            n_layers: Number of residual quantization layers
            n_embeddings: Number of embeddings per quantizer
            embedding_dim: Dimension of embeddings
        """
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.latent_dim = latent_dim
        self.n_layers = n_layers
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Latent space projections
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_var = nn.Linear(hidden_dim, latent_dim)
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim)
        )
        
        # Residual quantizers for each layer
        self.quantizers = nn.ModuleList([
            ResidualQuantizer(latent_dim, n_embeddings, embedding_dim)
            for _ in range(n_layers)
        ])
        
        # Layer normalization for residuals
        self.layer_norms = nn.ModuleList([
            nn.LayerNorm(latent_dim) for _ in range(n_layers)
        ])
        
    def encode(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Encode input to latent space
        
        Args:
            x: Input tensor
            
        Returns:
            mu: Mean of latent distribution
            log_var: Log variance of latent distribution
        """
        h = self.encoder(x)
        mu = self.fc_mu(h)
        log_var = self.fc_var(h)
        return mu, log_var
    
    def reparameterize(self, mu: torch.Tensor, log_var: torch.Tensor) -> torch.Tensor:
        """
        Reparameterization trick for sampling from latent distribution
        
        Args:
            mu: Mean of latent distribution
            log_var: Log variance of latent distribution
            
        Returns:
            Sampled latent vector
        """
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mu + eps * std
    
    def decode(self, z: torch.Tensor) -> torch.Tensor:
        """
        Decode latent vector to reconstruction
        
        Args:
            z: Latent vector
            
        Returns:
            Reconstructed output
        """
        return self.decoder(z)
    
    def residual_quantize(self, z: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Apply residual quantization to latent vector
        
        Args:
            z: Input latent vector
            
        Returns:
            quantized: Quantized latent vector
            total_loss: Total quantization loss
        """
        current_residual = z
        quantized = torch.zeros_like(z)
        total_loss = 0.0
        
        for i, (quantizer, layer_norm) in enumerate(zip(self.quantizers, self.layer_norms)):
            # Normalize residual
            normalized_residual = layer_norm(current_residual)
            
            # Quantize current residual
            layer_quantized, layer_loss, _ = quantizer(normalized_residual)
            
            # Add to total quantized output
            quantized += layer_quantized
            total_loss += layer_loss
            
            # Update residual for next layer
            current_residual = current_residual - layer_quantized
        
        return quantized, total_loss
    
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Forward pass through RQ VAE
        
        Args:
            x: Input tensor
            
        Returns:
            recon_x: Reconstructed input
            mu: Mean of latent distribution
            log_var: Log variance of latent distribution
            quant_loss: Quantization loss
        """
        # Encode
        mu, log_var = self.encode(x)
        
        # Sample from latent distribution
        z = self.reparameterize(mu, log_var)
        
        # Apply residual quantization
        quantized_z, quant_loss = self.residual_quantize(z)
        
        # Decode
        recon_x = self.decode(quantized_z)
        
        return recon_x, mu, log_var, quant_loss
    
    def loss_function(self, recon_x: torch.Tensor, x: torch.Tensor, 
                     mu: torch.Tensor, log_var: torch.Tensor, 
                     quant_loss: torch.Tensor, kld_weight: float = 1.0) -> torch.Tensor:
        """
        Calculate VAE loss
        
        Args:
            recon_x: Reconstructed input
            x: Original input
            mu: Mean of latent distribution
            log_var: Log variance of latent distribution
            quant_loss: Quantization loss
            kld_weight: Weight for KL divergence term
            
        Returns:
            Total loss
        """
        # Reconstruction loss
        recon_loss = F.mse_loss(recon_x, x, reduction='sum')
        
        # KL divergence loss
        kld_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
        
        # Total loss
        total_loss = recon_loss + kld_weight * kld_loss + quant_loss
        
        return total_loss


class RQVAETrainer:
    """
    Trainer class for RQ VAE
    """
    
    def __init__(self, model: RQVAE, device: str = 'cpu', 
                 learning_rate: float = 1e-3, kld_weight: float = 1.0):
        """
        Initialize trainer
        
        Args:
            model: RQ VAE model
            device: Device to train on
            learning_rate: Learning rate for optimizer
            kld_weight: Weight for KL divergence loss
        """
        self.model = model.to(device)
        self.device = device
        self.kld_weight = kld_weight
        
        self.optimizer = optim.Adam(model.parameters(), lr=learning_rate)
        self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, step_size=30, gamma=0.5)
        
        self.train_losses = []
        self.val_losses = []
        
    def train_epoch(self, dataloader: DataLoader) -> float:
        """
        Train for one epoch
        
        Args:
            dataloader: Training data loader
            
        Returns:
            Average training loss
        """
        self.model.train()
        total_loss = 0.0
        
        for batch_idx, (data, _) in enumerate(dataloader):
            data = data.to(self.device)
            self.optimizer.zero_grad()
            
            # Forward pass
            recon_batch, mu, log_var, quant_loss = self.model(data)
            
            # Calculate loss
            loss = self.model.loss_function(
                recon_batch, data, mu, log_var, quant_loss, self.kld_weight
            )
            
            # Backward pass
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
            
            if batch_idx % 100 == 0:
                print(f'Training batch {batch_idx}/{len(dataloader)}, Loss: {loss.item():.6f}')
        
        self.scheduler.step()
        return total_loss / len(dataloader)
    
    def validate(self, dataloader: DataLoader) -> float:
        """
        Validate model
        
        Args:
            dataloader: Validation data loader
            
        Returns:
            Average validation loss
        """
        self.model.eval()
        total_loss = 0.0
        
        with torch.no_grad():
            for data, _ in dataloader:
                data = data.to(self.device)
                
                # Forward pass
                recon_batch, mu, log_var, quant_loss = self.model(data)
                
                # Calculate loss
                loss = self.model.loss_function(
                    recon_batch, data, mu, log_var, quant_loss, self.kld_weight
                )
                
                total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    def train(self, train_loader: DataLoader, val_loader: DataLoader, 
              epochs: int = 100) -> None:
        """
        Train the model
        
        Args:
            train_loader: Training data loader
            val_loader: Validation data loader
            epochs: Number of training epochs
        """
        print("Starting training...")
        
        for epoch in range(epochs):
            # Training
            train_loss = self.train_epoch(train_loader)
            self.train_losses.append(train_loss)
            
            # Validation
            val_loss = self.validate(val_loader)
            self.val_losses.append(val_loss)
            
            print(f'Epoch {epoch+1}/{epochs}:')
            print(f'  Training Loss: {train_loss:.6f}')
            print(f'  Validation Loss: {val_loss:.6f}')
            print(f'  Learning Rate: {self.optimizer.param_groups[0]["lr"]:.6f}')
            print('-' * 50)
            
            # Save best model
            if epoch == 0 or val_loss < min(self.val_losses[:-1]):
                torch.save(self.model.state_dict(), 'best_rq_vae.pth')
                print("Saved best model!")
    
    def plot_losses(self):
        """Plot training and validation losses"""
        plt.figure(figsize=(10, 6))
        plt.plot(self.train_losses, label='Training Loss', alpha=0.8)
        plt.plot(self.val_losses, label='Validation Loss', alpha=0.8)
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.title('Training and Validation Losses')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()


def generate_synthetic_data(n_samples: int = 10000, input_dim: int = 64) -> torch.Tensor:
    """
    Generate synthetic data for demonstration
    
    Args:
        n_samples: Number of samples to generate
        input_dim: Dimension of input data
        
    Returns:
        Synthetic data tensor
    """
    # Generate data with multiple clusters
    n_clusters = 8
    samples_per_cluster = n_samples // n_clusters
    
    data = []
    for i in range(n_clusters):
        # Create cluster center
        center = torch.randn(input_dim) * 2.0
        center[i % input_dim] += 5.0  # Make clusters more distinct
        
        # Generate samples around center
        cluster_data = torch.randn(samples_per_cluster, input_dim) * 0.5 + center
        data.append(cluster_data)
    
    # Combine all clusters
    data = torch.cat(data, dim=0)
    
    # Shuffle data
    indices = torch.randperm(data.size(0))
    data = data[indices]
    
    return data


def demo_rq_vae():
    """Demonstrate RQ VAE on synthetic data"""
    
    # Set device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    # Generate synthetic data
    print("Generating synthetic data...")
    data = generate_synthetic_data(n_samples=10000, input_dim=64)
    
    # Split into train/validation
    train_size = int(0.8 * len(data))
    train_data = data[:train_size]
    val_data = data[train_size:]
    
    # Create data loaders
    train_dataset = TensorDataset(train_data, torch.zeros(len(train_data)))
    val_dataset = TensorDataset(val_data, torch.zeros(len(val_data)))
    
    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=128, shuffle=False)
    
    # Initialize model
    print("Initializing RQ VAE...")
    model = RQVAE(
        input_dim=64,
        hidden_dim=128,
        latent_dim=32,
        n_layers=3,
        n_embeddings=512,
        embedding_dim=64
    )
    
    # Initialize trainer
    trainer = RQVAETrainer(
        model=model,
        device=device,
        learning_rate=1e-3,
        kld_weight=1.0
    )
    
    # Train model
    trainer.train(train_loader, val_loader, epochs=50)
    
    # Plot training progress
    trainer.plot_losses()
    
    # Test reconstruction
    print("\nTesting reconstruction...")
    model.eval()
    with torch.no_grad():
        test_batch = val_data[:16].to(device)
        recon_batch, mu, log_var, quant_loss = model(test_batch)
        
        # Calculate reconstruction error
        mse = F.mse_loss(recon_batch, test_batch)
        print(f"Reconstruction MSE: {mse.item():.6f}")
        
        # Visualize some reconstructions
        plt.figure(figsize=(12, 4))
        for i in range(4):
            plt.subplot(2, 4, i + 1)
            plt.imshow(test_batch[i].cpu().view(8, 8), cmap='viridis')
            plt.title(f'Original {i+1}')
            plt.axis('off')
            
            plt.subplot(2, 4, i + 5)
            plt.imshow(recon_batch[i].cpu().view(8, 8), cmap='viridis')
            plt.title(f'Reconstructed {i+1}')
            plt.axis('off')
        
        plt.tight_layout()
        plt.show()
    
    return model, trainer, data


def simple_demo():
    """Simple demonstration without training"""
    print("Simple RQ VAE Demo")
    print("=" * 50)
    
    # Create a simple model
    model = RQVAE(
        input_dim=16,
        hidden_dim=32,
        latent_dim=8,
        n_layers=2,
        n_embeddings=64,
        embedding_dim=16
    )
    
    # Generate test data
    test_input = torch.randn(4, 16)
    print(f"Input shape: {test_input.shape}")
    
    # Forward pass
    model.eval()
    with torch.no_grad():
        recon_x, mu, log_var, quant_loss = model(test_input)
        
        print(f"Output shape: {recon_x.shape}")
        print(f"Latent mean shape: {mu.shape}")
        print(f"Latent variance shape: {log_var.shape}")
        print(f"Quantization loss: {quant_loss.item():.6f}")
        
        # Calculate reconstruction error
        mse = F.mse_loss(recon_x, test_input)
        print(f"Reconstruction MSE: {mse.item():.6f}")
    
    print("\nModel architecture:")
    print(model)
    
    return model


if __name__ == "__main__":
    # Run simple demo by default
    print("Running simple demo...")
    model = simple_demo()
    
    # Uncomment to run full training demo
    # print("\nRunning full training demo...")
    # model, trainer, data = demo_rq_vae()