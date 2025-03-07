"""
@Time: 2024/8/21 10:17
@Author: yanzx
@Desc:
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        length, right_most = len(nums), 0
        for i in range(len(nums)):
            if i <= right_most:  # i必须在能达到位置的左边
                right_most = max(right_most, i + nums[i])
                if right_most >= length - 1:
                    return True
            else:
                return False

    def canJump1(self, nums: List[int]) -> bool:
        """
        贪心算法，后边跳的总长度>=现在的总长度，就更新
        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return True

        i = 0
        while i < len(nums):
            cur = nums[i]
            cur_jump = i + nums[i]
            if cur_jump >= len(nums) - 1:  # 满足条件
                return True

            for j in range(i + 1, i + cur + 1):  # 查看后边的长度
                next_jump = j + nums[j]
                if next_jump >= cur_jump:  # 更新
                    cur_jump = next_jump
                    i = j
            if cur == 0:
                break
        return False


if __name__ == '__main__':
    s = Solution()

    nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    res = s.canJump(nums)
    print(res)
