"""
@Author: yanzx
@Date: 2025/3/8 10:46
@Description:
给你一个字符串 s，找到 s 中最长的 回文 子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


对于一个子串而言，如果它是回文串，并且长度大于 2，那么将它首尾的两个字母去除之后，它仍然是个回文串。例如对于字符串 “ababa”，如果我们已经知道 “bab” 是回文串，那么 “ababa” 一定是回文串，这是因为它的首尾两个字母都是 “a”。

根据这样的思路，我们就可以用动态规划的方法解决本题。我们用 P(i,j) 表示字符串 s 的第 i 到 j 个字母组成的串（下文表示成 s[i:j]）是否为回文串：

P(i,j)={
true,
false,
​

如果子串 S
i
​
 …S
j
​
  是回文串
其它情况
​

这里的「其它情况」包含两种可能性：

s[i,j] 本身不是一个回文串；

i>j，此时 s[i,j] 本身不合法。

那么我们就可以写出动态规划的状态转移方程：

P(i,j)=P(i+1,j−1)∧(S
i
​
 ==S
j
​
 )
也就是说，只有 s[i+1:j−1] 是回文串，并且 s 的第 i 和 j 个字母相同时，s[i:j] 才会是回文串。

上文的所有讨论是建立在子串长度大于 2 的前提之上的，我们还需要考虑动态规划中的边界条件，即子串的长度为 1 或 2。对于长度为 1 的子串，它显然是个回文串；对于长度为 2 的子串，只要它的两个字母相同，它就是一个回文串。因此我们就可以写出动态规划的边界条件：

{
P(i,i)=true
P(i,i+1)=(S
i
​
 ==S
i+1
​
 )
​

根据这个思路，我们就可以完成动态规划了，最终的答案即为所有 P(i,j)=true 中 j−i+1（即子串长度）的最大值。注意：在状态转移方程中，我们是从长度较短的字符串向长度较长的字符串进行转移的，因此一定要注意动态规划的循环顺序。

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        一定要写出来
        :param s:
        :return:
        """
        # 中心扩展法 O(n^2)
        max_right = 0
        max_left = 0
        # 以一个字母为中心
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            while left != -1 and right != len(s) and s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_left = left
                    max_right = right
                left -= 1
                right += 1
        # 以空洞为中心
        for i in range(len(s) - 1):
            left = i
            right = i + 1
            while left != -1 and right != len(s) and s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_left = left
                    max_right = right
                left -= 1
                right += 1
        return s[max_left: max_right + 1]

    def longestPalindrome_2nd(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # 1. 遍历字母为中心
        max_left, max_right = 0, 0
        for i in range(1, len(s)):
            left, right = i - 1, i + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_left = left
                    max_right = right
                left -= 1
                right += 1

        # 2. 遍历空洞为中心
        for i in range(0, len(s)):
            left, right = i, i + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_left = left
                    max_right = right
                left -= 1
                right += 1

        return s[max_left: max_right + 1]

    def longestPalindrome_dp(self, s: str) -> str:
        """
        使用动态规划方法
        dp[i][j]：表示s[i:j+1]是否为回文串
        :param s:
        :return:
        """
        n = len(s)
        if n < 2:
            return s

        # 初始化 dp 表
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1  # 初始化为第一个字符，长度为1

        # 单个字符一定是回文
        for i in range(n):
            dp[i][i] = True
        print(dp)
        # 填表，按子串长度从小到大
        for length in range(2, n + 1):  # 子串长度从2到n
            for i in range(n):  # 子串起始位置
                j = i + length - 1  # 子串结束位置，之所以要减1，是因为s[i:j]：j是闭区间
                if j >= n:  # 越界检查
                    break
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > max_len:
                            start = i
                            max_len = length
        return s[start:start + max_len]


    def longestPalindrome_dp_2nd(self, s: str) -> str:
        """
        1. 先固定长度，再固定字符

        :param s:
        :return:
        """
        n = len(s)
        if n < 2:
            return s
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for L in range(2, n + 1): # 先固定长度
            for i in range(n): # 再看字符
                j = i + L - 1
                print(i, j)
                if j >= n:
                    break
                if s[i] != s[j]:
                    continue
                if L == 2 or dp[i + 1][j-1]:
                    dp[i][j] = True
                    if L > max_len:
                        start = i
                        max_len = L
        return s[start: start+max_len]



if __name__ == '__main__':
    s = Solution()
    res = s.longestPalindrome_dp_2nd("abccv")
    print(res)
