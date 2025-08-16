from magic_stone_shortest_path import solve_magic_stone_path

def test_example():
    """测试题目给出的示例"""
    print("测试示例:")
    n, m, k = 5, 5, 2
    magic_stones = [0, 0, 0, -10, 0]
    roads = [
        (1, 2, 1),
        (2, 3, 1),
        (3, 5, 1),
        (1, 4, 1),
        (4, 5, 1)
    ]
    
    result = solve_magic_stone_path(n, m, k, magic_stones, roads)
    print(f"输入: n={n}, m={m}, k={k}")
    print(f"魔法石: {magic_stones}")
    print(f"道路: {roads}")
    print(f"输出: {result}")
    print(f"期望: -13")
    print()

def test_simple_cases():
    """测试简单情况"""
    print("测试简单情况:")
    
    # 测试1：只有坏魔法石
    n1, m1, k1 = 3, 2, 1
    magic_stones1 = [0, 5, 0]
    roads1 = [(1, 2, 1), (2, 3, 1)]
    
    result1 = solve_magic_stone_path(n1, m1, k1, magic_stones1, roads1)
    print(f"只有坏魔法石: {result1}")
    
    # 测试2：只有好魔法石
    n2, m2, k2 = 3, 2, 1
    magic_stones2 = [0, -2, 0]
    roads2 = [(1, 2, 1), (2, 3, 1)]
    
    result2 = solve_magic_stone_path(n2, m2, k2, magic_stones2, roads2)
    print(f"只有好魔法石: {result2}")
    
    # 测试3：无法到达
    n3, m3, k3 = 3, 1, 1
    magic_stones3 = [0, 0, 0]
    roads3 = [(1, 2, 1)]  # 没有到城市3的路
    
    result3 = solve_magic_stone_path(n3, m3, k3, magic_stones3, roads3)
    print(f"无法到达: {result3}")

if __name__ == "__main__":
    test_example()
    test_simple_cases()
