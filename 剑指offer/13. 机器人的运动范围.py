"""
@Author: yanzx
@Date: 2021-08-04 10:23:04
@Desc:
地上有一个m行n列的方格，
从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。

例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

eg1:
输入：m = 2, n = 3, k = 1
输出：3

eg2:
输入：m = 3, n = 1, k = 0
输出：1

当k = 8;
   0 1  2  3 4  5 6  7 8 9 10
0 可 可 可 可 可 可 可 可 可 不 可
1 可 可 可 可 可 可 可 可 不 不 可
2 可 可 可 可 可 可 可 不 不 不 可
3 可 可 可 可 可 可 不 不 不 不 可
4 可 可 可 可 可 不 不 不 不 不 可
5 可 可 可 可 不 不 不 不 不 不 可
6 可 可 可 不 不 不 不 不 不 不 可                      （可为可到达的，不为不可到达的）
7 可 可 不 不 不 不 不 不 不 不 可
8 可 不 不 不 不 不 不 不 不 不 不
9 不 不 不 不 不 不 不 不 不 不 不
10可 可 可 可 可 可 可 可 可 可 不

"""

# 暴力dfs，与12题差不多，走过的地方需要标记

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.res = 0
        hashset = set()

        def dfs(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return
            li_i, li_j = list(map(int, " ".join(str(i)).split())), list(map(int, " ".join(str(j)).split()))
            if sum(li_i) + sum(li_j) <= k and (i, j) not in hashset:
                self.res += 1
                hashset.add((i, j))
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i - 1, j)
                dfs(i + 1, j)
        dfs(0, 0)
        return self.res




if __name__ == '__main__':
    m = 2
    n = 3
    k = 1
    s = Solution()
    res = s.movingCount(m, n, k)
    print(res)
