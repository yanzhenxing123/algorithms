"""
@Author: yanzx
@Date: 2021-10-04 14:15:51
@Desc:
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
输入：nums = [3,4,3,3]
输出：4
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                if hashmap[i] == 3:
                    hashmap.pop(i)
        return list(hashmap.keys())[0]


if __name__ == '__main__':
    s = Solution()
    res = s.singleNumber([3, 4, 3, 3])
    print(res)
