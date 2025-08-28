"""

416. 分割等和子集
中等
相关标签
相关企业
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5] target = 11
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：
   0     1      2      3      4       5     6      7     8      9      10      11
[[True, True, False, False, False, False, False, False, False, False, False, False],
 [True, True, False, False, False, True,  True,  False, False, False, False, False],
 [True, True, False, False, False, True,  True,  False, False, False, False, True],
 [True, True, False, False, False, True,  True,  False, False, False,  True,  True]]


输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        """
        暴力回溯
        :param nums:
        :return:
        """
        total_sum = sum(nums)

        # 如果总和是奇数，无法分割
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        def backtrack(index, current_sum):
            # 基本情况
            if current_sum == target:
                return True

            if current_sum > target or index >= n:
                return False

            # 选择当前元素
            if backtrack(index + 1, current_sum + nums[index]):
                return True

            # 不选择当前元素
            if backtrack(index + 1, current_sum):
                return True

            return False

        return backtrack(0, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]

    def canPartition_2nd(self, nums):
        """
        target = sum(nums) // 2
        返回false的情况：0.nums长度小于2 1. 和为奇数，2. 最大值大于target

        dp[i][j]: 表示从数组的 [0,i] 下标范围内选取若干个正整数（可以是 0 个）
        ，是否存在一种选取方案使得被选取的正整数的和等于 j。初始时，dp 中的全部元素都是 false。

        :param nums:
        :return:
        """
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[False] * (target + 1) for _ in range(n)]  # 多一个target，其实是0
        for i in range(n):
            dp[i][0] = True

        for i in range(1, n):
            num = nums[i]  # 当前值
            for j in range(1, target + 1):
                if j >= num:  # 可以选当前值，也可以不选 dp[i - 1][j - num]：选取当前值  dp[i - 1][j]：不选当前值
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        print(dp)

        return dp[n - 1][target]

    def canPartition_3rd(self, nums):
        """
        是01背包
        dp[i][j]: 表示从数组的 [0,i] 下标范围内选取若干个正整数（可以是 0 个）
        ，是否存在一种选取方案使得被选取的正整数的和等于 j。初始时，dp 中的全部元素都是 false。
        :param nums:
        :return:
        """
        sum_num = sum(nums)
        target = sum_num // 2
        if len(nums) < 2 or sum_num % 2 == 1 or max(nums) > target:
            return False
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n)]  # 多一列0

        for i in range(n):
            dp[i][0] = True  # 将第一列都初始化为0

        for i in range(0, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:  # 可选可不选
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 11, 5]
    res = s.canPartition_3rd(nums)
    print(res)
