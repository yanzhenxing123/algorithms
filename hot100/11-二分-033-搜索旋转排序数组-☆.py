"""
@Time: 2024/4/26 15:34
@Author: yanzx
@Desc: 相当于找到最小值

输入：nums = [4,5,0,1,2], target = 0
输出：4

非常重点的一道题

"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        :param nums:
        :param target:
        :return:
        """
        # 1. 找到最小的值 最小值肯定在右边 所以mid在右边的时候 right = mid
        left, right = 0, len(nums) - 1
        min_index = 0
        while left <= right:
            mid = (left + right) // 2
            # 如果中间的比左边大并且比右边小，则说明有序，并且min_index = left
            if nums[left] <= nums[mid] <= nums[right]:
                min_index = left
                break
            if nums[left] <= nums[mid]:  # mid min
                left = mid + 1
            # elif nums[mid] < nums[right]:  # min mid
            #     right = mid
            else:
                right = mid

        # 找到min_index
        if min_index == 0:
            left, right = 0, len(nums) - 1
        elif nums[0] <= target:
            left, right = 0, min_index - 1
        else:
            left, right = min_index, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search_2nd(self, nums: List[int], target: int) -> int:
        """
        二刷
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        # 找到最小值的索引
        min_index = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] <= nums[right]:  # 有序就行
                min_index = left
                break
            elif nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid

        if min_index == 0:
            left = 0
            right = len(nums) - 1
        elif nums[0] <= target:
            left = 0
            right = min_index - 1
        else:
            left = min_index
            right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1]
    target = 3
    res = s.search(nums, target)
    print(res)
