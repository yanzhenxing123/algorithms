import sys
read = sys.stdin.readline

class UnionFind:
    def __init__(self, size):
        self.fa = list(range(size + 1))
        self.cnt = [1] * (size + 1)

    def get(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.get(self.fa[x])
        return self.fa[x]

    def merge(self, u, v):
        fu, fv = self.get(u), self.get(v)
        if fu != fv:
            if self.cnt[fu] < self.cnt[fv]:
                fu, fv = fv, fu
            self.fa[fv] = fu
            self.cnt[fu] += self.cnt[fv]

def main():
    t = int(read().strip())
    for _ in range(t):
        n, m = map(int, read().split())
        arr1 = list(map(int, read().split()))
        arr2 = list(map(int, read().split()))

        uf = UnionFind(m)
        used = set()

        for i in range(n):
            if arr1[i] != arr2[i]:
                uf.merge(arr1[i], arr2[i])
                used.add(arr1[i])
                used.add(arr2[i])

        groups = {}
        for val in used:
            root = uf.get(val)
            groups.setdefault(root, []).append(val)

        res = 0
        for g in groups.values():
            res += len(g) - 1

        print(res)

if __name__ == "__main__":
    main()
