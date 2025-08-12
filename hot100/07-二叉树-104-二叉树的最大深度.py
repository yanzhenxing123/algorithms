"""
@Time: 2024/4/13 22:43
@Author: yanzx
@Desc: 
"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    
    
    def maxDepth_2nd(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        

    

if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.maxDepth(root)
    print(res)
