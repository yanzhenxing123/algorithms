"""
@Author: yanzx
@Date: 2020/10/13 17:30
@Description:
定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
假定每组输入只存在唯一答案。
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 排序
        sorted_nums = sorted(nums)
        # 无穷大初始化
        result = differ_min = float("inf")

        for i in range(0, len(nums) - 2):
            # 固定一个值
            fixed = i

            # 首尾指针
            start = i + 1
            end = len(nums) - 1

            while start < end:
                sum_tmp = sorted_nums[fixed] + sorted_nums[start] + sorted_nums[end]
                if sum_tmp == target:
                    return target

                elif sum_tmp < target:
                    differ = target - sum_tmp
                    if differ < differ_min:
                        differ_min = differ
                        result = sum_tmp
                    start += 1

                else:
                    differ = sum_tmp - target
                    if differ < differ_min:
                        differ_min = differ
                        result = sum_tmp
                    end -= 1
        return result



if __name__ == '__main__':
    nums = [1,2,4,8,16,32,64,128]
    s = Solution()
    result = s.threeSumClosest(nums, 82)
    print("*" * 10)

    print(result)
