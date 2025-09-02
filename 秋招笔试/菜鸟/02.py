import math
import json

def calculate_entropy(user_data):
    """
    计算用户阅读新闻类别的信息熵
    
    Args:
        user_data: 字典，键是用户ID，值是包含各类别阅读次数的字典
    
    Returns:
        字典，键是用户ID，值是包含信息熵的字典
    """
    result = {}
    
    for user_id, categories in user_data.items():
        # 计算总的阅读次数
        total_reads = sum(categories.values())
        
        # 如果总阅读次数为0，熵为0
        if total_reads == 0:
            result[user_id] = {"entropy": 0.0}
            continue
        
        # 计算信息熵
        entropy = 0.0
        for count in categories.values():
            if count > 0:  # 避免log(0)
                probability = count / total_reads
                entropy -= probability * math.log2(probability)
        
        # 保留3位小数
        result[user_id] = {"entropy": round(entropy, 3)}
    
    return result

input_str = input()
user_data = json.loads(input_str)
result = calculate_entropy(user_data)
print(json.dumps(result))




