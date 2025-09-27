
def solve():
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().strip().split())
        D_set = set(map(int, input().strip().split()))

        found = False
        res = None
        for a1 in range(1, 27):
            for a2 in range(1, 27):
                a3 = n - a1 - a2
                if 1 <= a3 <= 26:
                    if abs(a1 - a2) in D_set and abs(a2 - a3) in D_set:
                        # 转成字母
                        word = chr(a1 + 96) + chr(a2 + 96) + chr(a3 + 96)
                        if not found or word < res:
                            res = word
                            found = True
                        # 因为 a1, a2 从小到大枚举，第一个找到的就是字典序最小
                        # 但为了保险，可以在 a1 循环里找到就 break 两次
                        # 不过题目要求最小，我们可以在内层找到后直接跳出
            # 优化：如果已经找到，可以提前结束 a1 循环
            # 但注意：可能同一个 a1 有多个 a2，我们要取最小的 a2，所以第一次找到的就是最小
            if found:
                break

        if found:
            print(res)
        else:
            print("NO")

if __name__ == "__main__":
    solve()