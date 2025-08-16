import heapq
from collections import defaultdict

def solve_magic_stone_path(n, m, k, magic_stones, roads):
    """
    解决魔法石最短路径问题
    
    Args:
        n: 城市数量
        m: 道路数量  
        k: 好魔法石使用次数限制
        magic_stones: 魔法石能量值列表
        roads: 道路列表，每个元素为 (u, v, w)
    
    Returns:
        最小通行时间或 "NO"
    """
    # 构建邻接表
    graph = defaultdict(list)
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))  # 双向道路
    
    # 优先队列：(总时间, 当前城市, 已使用好魔法石次数)
    pq = [(0, 1, 0)]
    
    # 访问状态：(城市, 已使用好魔法石次数)
    visited = set()
    
    while pq:
        total_time, current_city, used_magic = heapq.heappop(pq)
        
        # 如果到达目标城市
        if current_city == n:
            return total_time
        
        # 检查访问状态
        state = (current_city, used_magic)
        if state in visited:
            continue
        visited.add(state)
        
        # 遍历所有相邻城市
        for next_city, base_time in graph[current_city]:
            # 计算到下一个城市的通行时间
            magic_effect = magic_stones[next_city - 1]  # 转换为0索引
            
            if magic_effect >= 0:
                # 坏魔法石，强制生效
                actual_time = base_time + magic_effect
                new_total_time = total_time + actual_time
                new_used_magic = used_magic
                
                # 添加到优先队列
                heapq.heappush(pq, (new_total_time, next_city, new_used_magic))
                
            else:
                # 好魔法石，可选择是否生效
                # 选择1：不使用好魔法石
                actual_time = base_time
                new_total_time = total_time + actual_time
                new_used_magic = used_magic
                
                heapq.heappush(pq, (new_total_time, next_city, new_used_magic))
                
                # 选择2：使用好魔法石（如果还有次数）
                if used_magic < k:
                    actual_time = base_time + magic_effect  # magic_effect < 0，所以是减少时间
                    new_total_time = total_time + actual_time
                    new_used_magic = used_magic + 1
                    
                    heapq.heappush(pq, (new_total_time, next_city, new_used_magic))
    
    return "NO"

def main():
    """主函数"""
    # 读取输入
    n, m, k = map(int, input().split())
    magic_stones = list(map(int, input().split()))
    
    roads = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        roads.append((u, v, w))
    
    # 解决问题
    result = solve_magic_stone_path(n, m, k, magic_stones, roads)
    print(result)

if __name__ == "__main__":
    main()
