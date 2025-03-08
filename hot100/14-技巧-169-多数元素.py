"""
@Author: yanzx
@Date: 2025/3/8 11:05
@Description:
169. 多数元素

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2


提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        同类加
        异类消杀
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]
        winner = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:  # 消杀完更新即可
                winner = nums[i]
            if winner == nums[i]:  # 同类+1
                count += 1
            else:  # 异类消杀
                count -= 1
        return winner


if __name__ == '__main__':
    nums = [3, 2, 3]
    s = Solution()
    res = s.majorityElement(nums)
    print(res)
