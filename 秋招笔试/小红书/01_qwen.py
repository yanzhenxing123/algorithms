def solve():
    import sys
    results = []
    T = int(input())  # 测试用例数量

    for _ in range(T):
        n, d = map(int, input().split())  # 数组长度和阈值
        arr = list(map(int, input().split()))  # 数组元素
        arr.sort()
        res = n
        i = 0
        while i < len(arr) - 1:
            if arr[i + 1] - arr[i] < d:
                res -= 2  # 删除一对元素
                i += 2  # 跳过下一个元素
            else:
                i += 1
        results.append(res)

    print('\n'.join(map(str, results)))


solve()