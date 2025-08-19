"""
@Time: 2024/8/22 11:25
@Author: yanzx
@Desc:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
"""



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        1. dp[i][j]：代表从[0][0]这个点到[i][j]可选择的路径
        2. dp[i][j] = dp[i][j-1] + dp[i-1][j]
        3. 第一行和第一列初始化为1即可
        :param m:
        :param n:
        :return:
        """
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    res = s.uniquePaths(3, 7)
    print(res)
