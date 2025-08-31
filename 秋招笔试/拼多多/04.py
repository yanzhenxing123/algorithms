"""
@Time: 2025/8/31 16:45
@Author: yanzx
@Description:


对于每组测试数据，在单独的一行里输出所需的最少操作数。

示例1

输入：
3
3 8
3 5 1
2 5 1
3 8
2 5 1
5 2 1
3 8
2 5 2
5 2 1


输出：
0
1
2

"""



import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            if self.size[fx] < self.size[fy]:
                fx, fy = fy, fx
            self.parent[fy] = fx
            self.size[fx] += self.size[fy]

def solve():
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        dsu = DSU(m)
        involved = set()

        for i in range(n):
            if a[i] != b[i]:
                dsu.union(a[i], b[i])
                involved.add(a[i])
                involved.add(b[i])

        comp = {}
        for x in involved:
            root = dsu.find(x)
            comp.setdefault(root, []).append(x)

        ans = 0
        for nodes in comp.values():
            # 真正需要的操作次数是 (len(nodes) - 已经自然匹配的边数)
            # 这里简化：一个分量的最少操作次数 = len(nodes) - 1
            ans += len(nodes) - 1

        print(ans)

if __name__ == "__main__":
    solve()
