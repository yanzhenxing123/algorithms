import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

class RQKMeans:
    """
    Residual Quantized K-Means implementation
    
    This algorithm combines residual quantization with K-Means clustering
    to improve clustering performance on high-dimensional data.
    """
    
    def __init__(self, n_clusters: int = 8, n_layers: int = 3, 
                 max_iter: int = 300, random_state: int = 42):
        """
        Initialize RQKMeans
        
        Args:
            n_clusters: Number of clusters per layer
            n_layers: Number of residual quantization layers
            max_iter: Maximum iterations for K-Means
            random_state: Random seed for reproducibility
        """
        self.n_clusters = n_clusters
        self.n_layers = n_layers
        self.max_iter = max_iter
        self.random_state = random_state
        
        # Storage for learned centroids and assignments
        self.centroids = []  # List of centroid arrays for each layer
        self.assignments = []  # List of assignment arrays for each layer
        self.residuals = []  # List of residual arrays for each layer
        
    def fit(self, X: np.ndarray) -> 'RQKMeans':
        """
        Fit RQKMeans to the data
        
        Args:
            X: Input data of shape (n_samples, n_features)
            
        Returns:
            self: Fitted RQKMeans instance
        """
        X = np.asarray(X, dtype=np.float64)
        n_samples, n_features = X.shape
        
        # Initialize residuals with original data
        current_residual = X.copy()
        
        for layer in range(self.n_layers):
            print(f"Training layer {layer + 1}/{self.n_layers}")
            
            # Apply K-Means to current residuals
            kmeans = KMeans(
                n_clusters=self.n_clusters,
                max_iter=self.max_iter,
                random_state=self.random_state + layer,
                n_init=10
            )
            
            # Fit K-Means and get assignments
            assignments = kmeans.fit_predict(current_residual)
            centroids = kmeans.cluster_centers_
            
            # Store results for this layer
            self.centroids.append(centroids)
            self.assignments.append(assignments)
            
            # Compute residuals for next layer
            reconstructed = centroids[assignments]
            current_residual = current_residual - reconstructed
            
            # Store residuals for analysis
            self.residuals.append(current_residual.copy())
            
            # Print layer statistics
            residual_norm = np.linalg.norm(current_residual, axis=1).mean()
            print(f"  Layer {layer + 1} - Mean residual norm: {residual_norm:.4f}")
        
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict cluster assignments for new data
        
        Args:
            X: Input data of shape (n_samples, n_features)
            
        Returns:
            assignments: Cluster assignments for each sample
        """
        X = np.asarray(X, dtype=np.float64)
        n_samples = X.shape[0]
        
        # Initialize assignments array
        final_assignments = np.zeros(n_samples, dtype=int)
        
        # Process each layer
        current_residual = X.copy()
        
        for layer in range(self.n_layers):
            # Find nearest centroid for current residuals
            distances = pairwise_distances(
                current_residual, 
                self.centroids[layer], 
                metric='euclidean'
            )
            layer_assignments = np.argmin(distances, axis=1)
            
            # Update final assignments (combine with previous layers)
            final_assignments = final_assignments * self.n_clusters + layer_assignments
            
            # Compute residuals for next layer
            reconstructed = self.centroids[layer][layer_assignments]
            current_residual = current_residual - reconstructed
        
        return final_assignments
    
    def reconstruct(self, X: np.ndarray) -> np.ndarray:
        """
        Reconstruct data using learned centroids
        
        Args:
            X: Input data of shape (n_samples, n_features)
            
        Returns:
            reconstructed: Reconstructed data
        """
        X = np.asarray(X, dtype=np.float64)
        n_samples = X.shape[0]
        
        reconstructed = np.zeros_like(X)
        current_residual = X.copy()
        
        for layer in range(self.n_layers):
            # Find nearest centroid
            distances = pairwise_distances(
                current_residual, 
                self.centroids[layer], 
                metric='euclidean'
            )
            assignments = np.argmin(distances, axis=1)
            
            # Add reconstruction from this layer
            reconstructed += self.centroids[layer][assignments]
            
            # Update residuals
            current_residual = current_residual - self.centroids[layer][assignments]
        
        return reconstructed
    
    def get_compression_ratio(self) -> float:
        """
        Calculate compression ratio achieved by RQKMeans
        
        Returns:
            compression_ratio: Ratio of original data size to compressed size
        """
        if not self.centroids:
            return 1.0
        
        # Calculate total number of centroids across all layers
        total_centroids = sum(centroids.shape[0] for centroids in self.centroids)
        total_centroid_values = sum(centroids.size for centroids in self.centroids)
        
        # For each sample, we need log2(n_clusters^layers) bits per layer
        bits_per_sample = self.n_layers * np.log2(self.n_clusters)
        
        # This is a simplified calculation - in practice, you'd need to account
        # for actual storage requirements of centroids and assignments
        return total_centroid_values / (len(self.centroids[0]) * self.n_layers)
    
    def visualize_layers(self, X: np.ndarray, max_samples: int = 1000):
        """
        Visualize the residual quantization layers
        
        Args:
            X: Input data for visualization
            max_samples: Maximum number of samples to plot
        """
        if X.shape[1] != 2:
            print("Visualization only works for 2D data")
            return
        
        # Subsample for visualization
        if X.shape[0] > max_samples:
            indices = np.random.choice(X.shape[0], max_samples, replace=False)
            X_viz = X[indices]
        else:
            X_viz = X
        
        fig, axes = plt.subplots(2, self.n_layers, figsize=(4*self.n_layers, 8))
        
        for layer in range(self.n_layers):
            # Plot original data and centroids
            axes[0, layer].scatter(X_viz[:, 0], X_viz[:, 1], alpha=0.6, s=20)
            axes[0, layer].scatter(
                self.centroids[layer][:, 0], 
                self.centroids[layer][:, 1], 
                c='red', s=100, marker='x', linewidths=3
            )
            axes[0, layer].set_title(f'Layer {layer + 1}: Data + Centroids')
            axes[0, layer].grid(True, alpha=0.3)
            
            # Plot residuals
            if layer < len(self.residuals):
                axes[1, layer].scatter(
                    self.residuals[layer][:max_samples, 0], 
                    self.residuals[layer][:max_samples, 1], 
                    alpha=0.6, s=20
                )
                axes[1, layer].set_title(f'Layer {layer + 1}: Residuals')
                axes[1, layer].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()


def demo_rqkmeans():
    """Demonstrate RQKMeans on synthetic data"""
    
    # Generate synthetic 2D data with multiple clusters
    np.random.seed(42)
    n_samples = 2000
    n_features = 2
    
    # Create multiple Gaussian clusters
    centers = [
        [0, 0], [4, 4], [-3, 3], [3, -3], [-2, -2],
        [6, 0], [0, 6], [-4, -4], [8, 8], [-8, -8]
    ]
    
    X = np.random.randn(n_samples, n_features) * 0.5
    for i, center in enumerate(centers):
        start_idx = i * (n_samples // len(centers))
        end_idx = (i + 1) * (n_samples // len(centers))
        X[start_idx:end_idx] += center
    
    # Initialize and fit RQKMeans
    print("Training RQKMeans...")
    rqkmeans = RQKMeans(n_clusters=8, n_layers=3, random_state=42)
    rqkmeans.fit(X)
    
    # Get predictions and reconstructions
    assignments = rqkmeans.predict(X)
    reconstructed = rqkmeans.reconstruct(X)
    
    # Calculate reconstruction error
    mse = np.mean((X - reconstructed) ** 2)
    print(f"\nReconstruction MSE: {mse:.6f}")
    
    # Calculate compression ratio
    compression_ratio = rqkmeans.get_compression_ratio()
    print(f"Compression ratio: {compression_ratio:.2f}")
    
    # Visualize results
    print("\nGenerating visualizations...")
    rqkmeans.visualize_layers(X)
    
    # Plot final clustering results
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=assignments, alpha=0.6, s=20)
    plt.title('RQKMeans Clustering Results')
    plt.colorbar()
    
    plt.subplot(1, 2, 2)
    plt.scatter(reconstructed[:, 0], reconstructed[:, 1], alpha=0.6, s=20)
    plt.title('Reconstructed Data')
    
    plt.tight_layout()
    plt.show()
    
    return rqkmeans, X, assignments, reconstructed


if __name__ == "__main__":
    # Run demonstration
    rqkmeans, X, assignments, reconstructed = demo_rqkmeans()
