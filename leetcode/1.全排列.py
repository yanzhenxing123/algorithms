import sys
sys.setrecursionlimit(10000)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.backtrack(nums, [])
        return self.res


    def backtrack(self, nums, path):
        if len(nums) == len(path):
            self.res.append(path.copy())
            return

        for i in nums:
            if i not in path:
                path.append(i)
                self.backtrack(nums, path)
                path.pop()



if __name__ == '__main__':
    s = Solution()
    res = s.permute([1, 2, 3])
    print(res)