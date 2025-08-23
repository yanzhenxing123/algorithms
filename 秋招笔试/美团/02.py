import json
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def dbscan_anomaly_detector(input_json):
    """
    DBSCAN异常检测器
    
    实现步骤：
    1. 将train和test数据合并后进行标准化
    2. 在标准化后的合并数据上应用DBSCAN聚类
    3. 对簇标签进行重映射（按质心第一个维度排序）
    4. 输出test数据的重映射标签
    
    Args:
        input_json (str): JSON格式的输入字符串
        
    Returns:
        list: 测试样本的聚类标签
    """
    # 解析输入JSON
    data = json.loads(input_json)
    train_data = np.array(data['train'])
    test_data = np.array(data['test'])
    
    # 1. 数据预处理：将train和test数据连接
    combined_data = np.vstack([train_data, test_data])
    
    # 2. 标准化：使用StandardScaler对合并后的数据进行一次fit_transform
    scaler = StandardScaler()
    combined_scaled = scaler.fit_transform(combined_data)
    
    # 3. DBSCAN聚类：在合并后的标准化数据上应用
    dbscan = DBSCAN(
        eps=0.3,
        min_samples=3,
        metric='euclidean',
        algorithm='auto'
    )
    
    # 在合并后的标准化数据上拟合DBSCAN
    dbscan.fit(combined_scaled)
    
    # 获取所有数据的聚类标签
    all_labels = dbscan.labels_
    
    # 分离train和test的标签
    train_labels = all_labels[:len(train_data)]
    test_labels = all_labels[len(train_data):]
    
    # 4. 簇标签重映射
    # 获取所有非异常簇的标签（从所有数据中）
    unique_labels = np.unique(all_labels)
    non_outlier_labels = unique_labels[unique_labels != -1]
    
    if len(non_outlier_labels) > 0:
        # 计算每个簇的质心（使用所有数据）
        centroids = []
        for label in non_outlier_labels:
            cluster_points = combined_scaled[all_labels == label]
            centroid = np.mean(cluster_points, axis=0)
            centroids.append((label, centroid))
        
        # 按第一个维度排序簇
        centroids.sort(key=lambda x: x[1][0])
        
        # 创建标签映射字典
        label_mapping = {}
        for new_label, (old_label, _) in enumerate(centroids):
            label_mapping[old_label] = new_label
        
        # 异常点保持-1标签
        label_mapping[-1] = -1
        
        # 重映射test标签
        test_labels_remapped = [int(label_mapping[label]) for label in test_labels]
        
        return test_labels_remapped
    else:
        # 如果没有找到有效簇，所有test点都标记为异常
        return [-1] * len(test_data)

def main():
    """
    主函数：处理标准输入并输出结果
    """
    try:
        # 读取标准输入
        input_line = input().strip()
        
        # 调用异常检测器
        result = dbscan_anomaly_detector(input_line)
        print(result)
        
        # 输出结果（确保符合JSON格式，逗号后有空格）
        # print(json.dumps(result, separators=(', ', '')))
        
    except Exception as e:
        # 错误处理
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main()
