"""
6
4 5
1 2 4 3
4 6
1 2 4 3
5 20
2 7 1 8 2
2 2
3 2
2 15
1 5
2 7
5 2

"""

def count_sinking_ships(n, ships, attacks):
    # Create a list to track the current durability of each ship
    durability = ships[:]

    # Initialize the count of sinking ships
    sinking_ships = 0

    # Process each attack
    for attack in attacks:
        for i in range(n):
            if durability[i] > 0:
                durability[i] -= attack
                if durability[i] <= 0:
                    sinking_ships += 1
                    break  # A ship sinks, move on to the next attack

    return sinking_ships


def main():
    """主函数"""
    # 读取测试用例数量
    t = int(input())

    # 处理每个测试用例
    for _ in range(t):
        # 读取n和k
        n, k = map(int, input().split())

        # 读取耐久度数组
        a = list(map(int, input().split()))

        # 计算结果
        result = solve_deep_sea_math_simple(n, k, a)

        # 输出结果
        print(result)


if __name__ == "__main__":
    main()
