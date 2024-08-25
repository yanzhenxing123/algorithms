"""
@Time: 2024/8/25 10:54
@Author: yanzx
@Desc:

"""


def main():
    """
    i代表物品，j代表容量
    :return:
    """
    n, bagweight = map(int, input().split())

    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))

    dp = [[0] * (bagweight + 1) for _ in range(n)]

    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    for i in range(1, n):
        for j in range(bagweight + 1):
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    print(dp[n - 1][bagweight])


if __name__ == '__main__':
    main()
