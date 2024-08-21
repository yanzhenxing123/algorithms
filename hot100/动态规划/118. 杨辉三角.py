"""
@Time: 2024/8/21 16:56
@Author: yanzx
@Desc:
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1, 1])
        if numRows == 2:
            return res
        for i in range(2, numRows):
            cur_nums = [1]
            last_nums = res[-1]
            for j in range(1, len(last_nums)):
                cur_nums.append(last_nums[j - 1] + last_nums[j])
            cur_nums.append(1)
            res.append(cur_nums)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.generate(numRows=5)
    print(res)
