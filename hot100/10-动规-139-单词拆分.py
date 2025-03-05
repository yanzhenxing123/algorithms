"""
@Author: yanzx
@Date: 2025/3/4 11:33
@Description:

给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。



示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

dp[i] 表示已s[0:i+1] 能否被表示


输入: s = "applepenapple", wordDict = ["apple", "pen"]
    " a p p l e p e n a p p l e"
dp = [F,F,F,F,T,F,F,T,F,F,F,F,T]


"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if not wordDict:
            return False
        n = len(s)
        dp = [False] * n
        if s[1] in wordDict:
            dp[0] = True
        for i in range(0, n):  # 固定当前字符
            for j in range(i + 1, n + 1):
                if i == 0 and (s[i:j] in wordDict):
                    dp[j - 1] = True
                elif dp[i - 1] and (s[i:j] in wordDict):
                    dp[j - 1] = True
            print(dp)
        return dp[-1]


if __name__ == '__main__':
    string = "applepenapple"
    wordDict = ["apple", "pen"]
    s = Solution()
    res = s.wordBreak(string, wordDict)
    print(res)
