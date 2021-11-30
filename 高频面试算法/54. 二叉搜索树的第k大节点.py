"""
@Author: yanzx
@Date: 2021-10-05 13:24:21
@Desc: 
"""
from utils.binary_tree import TreeNode, create_tree, floor_print


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.res = 0

        def dfs(root: TreeNode):
            if root:
                dfs(root.right)
                self.count += 1
                if self.count == k:
                    self.res = root.val
                dfs(root.left)

        dfs(root)
        return self.res

if __name__ == '__main__':
    s = Solution()
    nums = [5, 3, 6, 2, 4, None, None, 1]
    k = 3
    root = create_tree(nums)
    res = s.kthLargest(root, k)
    print(res)
