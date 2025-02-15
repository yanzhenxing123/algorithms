"""
@Time: 2024/3/22 22:47
@Author: yanzx
@Desc:

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

不会做

维护一个hash列表，记录的是当前元素的连续的值，然后更新端点(left和right的值)

维护一个left和right

"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        只记录端点的length
        :param nums:
        :return:
        """
        max_length = 0
        hash_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            print(hash_dict)
            if num in hash_dict:
                continue
            left = hash_dict.get(num - 1, 0)  # 左边的长度
            right = hash_dict.get(num + 1, 0)  # 右边的长度
            cur_len = right + left + 1
            hash_dict[num] = cur_len
            if cur_len > max_length:
                max_length = cur_len
            # 更新左边和右边的值
            hash_dict[num - left] = cur_len
            hash_dict[num + right] = cur_len
        return max_length

    def longestConsecutive2(self, nums: List[int]) -> int:
        """
        官方题目给的最优解
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:  # num-1没在num_set中说明此数字是序列中的第一个
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak


if __name__ == '__main__':
    s = Solution()
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    res = s.longestConsecutive2(nums)
    print(res)
