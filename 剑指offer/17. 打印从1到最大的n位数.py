"""
@Author: yanzx
@Date: 2021/8/18 0:04
@Description: 
"""

from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max_num = "".join(["9" for _ in range(n)])
        return [i for i in range(1, int(max_num) + 1)]

if __name__ == '__main__':
    s = Solution()
    res = s.printNumbers(3)
    print(res)

