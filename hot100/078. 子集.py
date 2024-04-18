"""
@Time: 2024/4/18 10:23
@Author: yanzx
@Desc:





示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

"""

from typing import List





if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    res = s.subsets(nums)
    print(res)
