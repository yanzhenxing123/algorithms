"""
@Time: 2024/8/21 10:47
@Author: yanzx
@Desc:

给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        length, right_most = len(nums), 0

        i = 0
        count = 0
        while i < len(nums) - 1:
            # 1. 跳
            right_most = i + nums[i]
            count += 1
            if right_most >= length - 1:  # 终止条件
                return count
            # 2. 看后边的更新 i
            for j in range(i + 1, i + nums[i] + 1):
                if right_most <= j + nums[j]:
                    i = j
                    right_most = j + nums[j]
        return count

    def jump_2nd(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        count = 0
        index = 0
        length = len(nums)
        right_most = 0
        while index < length - 1:
            # 1. 跳
            right_most = index + nums[index]
            count += 1
            if right_most >= length - 1:
                return count
            # 2. 更新最大的right_most
            for j in range(index + 1, right_most + 1):
                cur_jump_dis = j + nums[j]
                if cur_jump_dis >= right_most:
                    index = j
                    right_most = cur_jump_dis

        return count


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    res = s.jump(nums)
    print(res)
