<<<<<<< HEAD
print("aaa")
=======
"""
this is a test py
"""

# 这是一个使用DataLoader的Demo
import torch.nn as nn
import torch
import torch.utils.data as data

# 特征数据：花朵的大小（第一列）和颜色（第二列）
features = torch.tensor([
    [5.1, 1.4],
    [4.9, 1.4],
    [5.8, 1.7],
    [6.0, 1.4],
    [5.5, 1.3],
    [5.4, 1.7]
])

# 标签：0表示玫瑰，1表示向日葵
labels = torch.tensor([0, 0, 1, 1, 0, 1])


# 创建自定义的数据集类
class FlowerDataset(data.Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels

    def __len__(self):
        return len(self.features)

    def __getitem__(self, index):
        return self.features[index], self.labels[index]


# 创建数据集
flower_dataset = FlowerDataset(features, labels)

# 创建 DataLoader 对象
batch_size = 2
flower_loader = data.DataLoader(flower_dataset, batch_size=batch_size, shuffle=True)

# 遍历数据集，观察每个批次中的数据
for inputs, labels in flower_loader:
    print("Batch Features:")
    print(inputs)
    print("Batch Labels:")
    print(labels)
    print("-----------------------")


# 我感觉这兼职就是一种折磨 对于我来说 不知道 为为什么

print("aaa")
>>>>>>> 11c05c0ecf58bf12586279899c2dc706883f8f6d
