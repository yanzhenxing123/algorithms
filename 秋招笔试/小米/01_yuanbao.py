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

import sys


def main():
    t = int(input())

    # 处理每个测试用例
        # 读取n和k

    results = []

    for _ in range(t):
        n, k = map(int, input().split())

        # 读取耐久度数组
        a = list(map(int, input().split()))



        left = 0
        right = n - 1
        sunk = 0

        while left <= right and k > 0:
            if left == right:
                # 只剩一艘船
                if a[left] <= k:
                    sunk += 1
                break

            if a[left] < a[right]:
                # 左端耐久度较小
                attacks_needed = 2 * a[left] - 1
                if k >= attacks_needed:
                    k -= attacks_needed
                    a[right] -= (a[left] - 1)
                    sunk += 1
                    left += 1
                else:
                    break
            else:
                # 右端耐久度较小或相等
                attacks_needed = 2 * a[right]
                if k >= attacks_needed:
                    k -= attacks_needed
                    a[left] -= a[right]
                    sunk += 1
                    right -= 1
                else:
                    break

        results.append(str(sunk))

    print("\n".join(results))




if __name__ == '__main__':
    main()