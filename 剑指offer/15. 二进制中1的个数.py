"""
@Author: yanzx
@Date: 2021-08-17 14:44:04
@Desc: 
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        bn = bin(n)
        return bn.count("1")

if __name__ == '__main__':
    s = Solution()
    n = 0b0000000000000000000000000001011
    res = s.hammingWeight(n)
    print(res)
