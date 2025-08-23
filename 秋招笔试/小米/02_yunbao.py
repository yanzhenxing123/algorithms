import sys

"""
3
1 1
2
5 1
1 2 4 7 8
5 3
6 4 7 10 5

"""


def can_achieve(x, h, k):
    n = len(h)
    count = 0
    for i in range(n - 1):
        diff = abs(h[i + 1] - h[i])
        if diff > x:
            count += 1
            if count > k:
                return False
    return True


def main():
    T = int(input())

    # 处理每个测试用例
    for _ in range(T):
        # 读取n和k
        n, k = map(int, input().split())

        # 读取山的高度
        h = list(map(int, input().split()))

        results = []

        left, right = 0, max(h)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can_achieve(mid, h, k):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        # results.append(str(ans))

        print(ans)

    # print("\n".join(results))


if __name__ == "__main__":
    main()