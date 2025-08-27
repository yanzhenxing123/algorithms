import torch
import torch.nn as nn
import torch.nn.functional as F


class ResidualQuantizer(nn.Module):
    """残差量化器"""

    def __init__(self, input_dim, n_embeddings=512, embedding_dim=64):
        super().__init__()
        self.embedding = nn.Embedding(n_embeddings, embedding_dim)
        self.input_proj = nn.Linear(input_dim, embedding_dim)
        self.output_proj = nn.Linear(embedding_dim, input_dim)

    def forward(self, inputs):
        # 投影到嵌入空间
        flat_input = self.input_proj(inputs.view(-1, inputs.size(-1)))

        # 计算距离，找到最近嵌入
        distances = torch.cdist(flat_input, self.embedding.weight)
        encoding_indices = torch.argmin(distances, dim=1)

        # 量化
        quantized = self.embedding(encoding_indices)
        quantized = self.output_proj(quantized)

        # Straight-through estimator
        quantized = inputs + (quantized - inputs).detach()

        return quantized


class RQVAE(nn.Module):
    """残差量化VAE"""

    def __init__(self, input_dim, hidden_dim=128, latent_dim=32, n_layers=3):
        super().__init__()

        # 编码器
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, latent_dim)
        )

        # 解码器
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim)
        )

        # 残差量化器
        self.quantizers = nn.ModuleList([
            ResidualQuantizer(latent_dim) for _ in range(n_layers)
        ])

    def forward(self, x):
        # 编码
        z = self.encoder(x)

        # 残差量化
        quantized = torch.zeros_like(z)
        residual = z

        for quantizer in self.quantizers:
            layer_quantized = quantizer(residual)
            quantized += layer_quantized
            residual = residual - layer_quantized

        # 解码
        recon_x = self.decoder(quantized)

        return recon_x, z, quantized


# 训练函数
def train_rq_vae(model, dataloader, epochs=10):
    optimizer = torch.optim.Adam(model.parameters())
    criterion = nn.MSELoss()

    for epoch in range(epochs):
        total_loss = 0
        for batch in dataloader:
            optimizer.zero_grad()

            recon_x, z, quantized = model(batch)

            # 重构损失 + 量化损失
            loss = criterion(recon_x, batch) + 0.1 * criterion(quantized, z)

            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f'Epoch {epoch + 1}, Loss: {total_loss / len(dataloader):.4f}')