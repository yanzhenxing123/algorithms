"""
@Author: yanzx
@Date: 2024/12/1 18:35
@Description:


       3, 2, 1, 4, 7
    0  0  0  0  0  0
1,  0  0  0  1  0  0
2,  0  0  1  0  0  0
3,  0  1  0  0  0  0
2,  0  0  2  0  0  0
1   0  0  0  3  0  0

dp[i][j] 表示 nums1[:i] 和 num[:j]最长的公共后缀

最后max即可

"""

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        m = len(nums1)
        n = len(nums2)
        dp = [
            [0 for _ in range(n + 1)] for _ in range(m + 1)
        ]
        nums1 = [0] + nums1
        nums2 = [0] + nums2

        res = 0

        for i in range(1, m + 1):
            # 固定num1中元素
            number1 = nums1[i]
            for j in range(1, n + 1):
                number2 = nums2[j]
                if number1 == number2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(dp[i][j], res)

                # else: # 一定是没有的 不然成子序列了
                #     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print(dp)
        return res


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    res = s.findLength(nums1, nums2)
    print(res)
