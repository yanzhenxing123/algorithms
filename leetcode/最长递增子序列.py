"""
@Author: yanzx
@Date: 2021/3/22 21:16
@Description:

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

倒序 逆着来

[0,3,1,6,2,2,7]
[1,1,1,1,1,1,1]

方法二：维护一个数组，数组的递增的最慢
eg：[0,3,1,6,2,2,7]
[0]
[0,3]
[0,1]
[0,1,6]
[0,1,2]
[0,1,2]
[0,1,2,7]

"""

from typing import List

class Solution:
    # 动态规划
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1 for _ in range(length)]
        for i in range(1, length):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            print(dp)
        return max(dp)

    # 贪心
    def lengthOfLIS_binery_search(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if not arr or arr[-1] < num:
                arr.append(num)
            else:
                l, r = 0, len(arr)
                # 二分插入
                while l < r:
                    mid = (l + r) // 2
                    if arr[mid] == num:
                        break
                    if arr[mid] > num:
                        r = mid
                    else:
                        l = mid + 1
                if arr[mid] >= num:
                    arr[mid] = num
                else:
                    arr[mid+1] = num
        return len(arr)


if __name__ == '__main__':
    s = Solution()
    nums = [0,3,1,6,2,2,7]
    res = s.lengthOfLIS(nums)
    print(res)
