"""
@Author: yanzx
@Date: 2021-10-06 19:51:51
@Desc:
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
即B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

解题思路：构建一个双指针

"""

from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = [1 for _ in range(len(a))]
        left, right = 0, len(a) - 1
        left_sum, right_sum = 1, 1
        while left < len(a):
            res[left] *= left_sum
            res[right] *= right_sum

            left_sum *= a[left]
            right_sum *= a[right]

            left += 1
            right -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.constructArr([1, 2, 3, 4, 5])
    print(res)
