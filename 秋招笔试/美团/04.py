import sys

sys.setrecursionlimit(1 << 20)
from collections import defaultdict


class FinalOptimizedTreeRedPoints:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(n + 1)]  # 1-indexed, (to, w)

        # 点分治用
        self.removed = [False] * (n + 1)
        self.sz = [0] * (n + 1)

        # 每个节点的重心链路径：[(centroid, dist_to_centroid, child_block_id)]
        # child_block_id: 在该重心下，节点属于哪个子块（用于容斥）；重心自身用 -1
        self.paths = [[] for _ in range(n + 1)]

        # 对每个重心的全局统计
        self.cnt = [0] * (n + 1)  # 红点数
        self.sumDist = [0] * (n + 1)  # 到该重心的距离和

        # 对每个 (centroid, child_block_id) 的子块统计（容斥）
        self.subCnt = defaultdict(int)
        self.subSum = defaultdict(int)

        # 红点状态
        self.is_red = [False] * (n + 1)

    def add_edge(self, u, v, w):
        self.tree[u].append((v, w))
        self.tree[v].append((u, w))

    # ---------- 点分治构建 ----------
    def _calc_size(self, u, p):
        self.sz[u] = 1
        for v, w in self.tree[u]:
            if v == p or self.removed[v]:
                continue
            self._calc_size(v, u)
            self.sz[u] += self.sz[v]

    def _find_centroid(self, u, p, tot):
        # 返回以 u 为根、总大小 tot 的子树的重心
        for v, w in self.tree[u]:
            if v != p and (not self.removed[v]) and self.sz[v] > tot // 2:
                return self._find_centroid(v, u, tot)
        return u

    def _collect_and_fill_paths(self, start, p, dist_acc, centroid, child_block_id):
        # 从某个分支出发 DFS，收集每个节点到重心的距离，并记录路径项
        self.paths[start].append((centroid, dist_acc, child_block_id))
        for v, w in self.tree[start]:
            if v == p or self.removed[v]:
                continue
            self._collect_and_fill_paths(v, start, dist_acc + w, centroid, child_block_id)

    def _build_centroid(self, entry):
        self._calc_size(entry, 0)
        c = self._find_centroid(entry, 0, self.sz[entry])
        self.removed[c] = True

        # 重心自身路径（dist=0，子块=-1）
        self.paths[c].append((c, 0, -1))

        # 给每个“从重心出发的子树”分配一个 child_block_id
        block_id = 0
        for v, w in self.tree[c]:
            if self.removed[v]:
                continue
            block_id += 1
            # 以 v 为根的这个分支里所有点到重心 c 的距离：dist + w
            self._collect_and_fill_paths(v, c, w, c, block_id)

        # 递归处理每个子树
        for v, w in self.tree[c]:
            if self.removed[v]:
                continue
            self._build_centroid(v)

        # 解除标记（不需要恢复，点分治常用“永久 removed”）
        # 这里不恢复是对的：removed 只是用于构建过程中的剪枝

    def build_index(self, root=1):
        """构建点分治索引与每点到各重心的距离"""
        self._build_centroid(root)

    # ---------- 维护（切红点）与查询 ----------
    def _activate(self, u):
        if self.is_red[u]:
            return
        self.is_red[u] = True
        for c, d, bid in self.paths[u]:
            self.cnt[c] += 1
            self.sumDist[c] += d
            if bid != -1:
                key = (c, bid)
                self.subCnt[key] += 1
                self.subSum[key] += d

    def _deactivate(self, u):
        if not self.is_red[u]:
            return
        self.is_red[u] = False
        for c, d, bid in self.paths[u]:
            self.cnt[c] -= 1
            self.sumDist[c] -= d
            if bid != -1:
                key = (c, bid)
                self.subCnt[key] -= 1
                self.subSum[key] -= d

    def toggle_red_point(self, v):
        if self.is_red[v]:
            self._deactivate(v)
        else:
            self._activate(v)

    def calculate_distance_sum(self, v):
        # 空集
        # （如果没有红点，沿路径加出来也会是 0，这里直接判断更快）
        # 但我们没有全局红点总数，简单判断某一层也不稳妥；可以快速探测：看任一重心 cnt 是否>0。
        # 为了常数更小，这里不做额外遍历，直接按公式算，若全 0 结果自然是 0。
        ans = 0
        for c, d, bid in self.paths[v]:
            # 加上所有红点通过该重心的贡献
            ans += self.sumDist[c] + self.cnt[c] * d
            # 减去和 v 同属该重心的同一子块的贡献（容斥）
            if bid != -1:
                key = (c, bid)
                ans -= self.subSum[key] + self.subCnt[key] * d
        return ans

    # 兼容你的输入：一次性设置初始红点
    def set_initial_red_points(self, red_status):
        for i in range(1, self.n + 1):
            if red_status[i - 1] == 1:
                self._activate(i)


# ---------------- I/O ----------------
def solve():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    red_status = list(map(int, input().split()))

    tree = FinalOptimizedTreeRedPoints(n)
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        tree.add_edge(u, v, w)

    # 预处理：点分治 + 距离索引（O(N log N)），之后每次 O(log N)
    tree.build_index()
    tree.set_initial_red_points(red_status)

    for _ in range(q):
        t, v = map(int, input().split())
        if t == 1:
            tree.toggle_red_point(v)
        else:  # t == 2
            print(tree.calculate_distance_sum(v))


if __name__ == "__main__":
    solve()
