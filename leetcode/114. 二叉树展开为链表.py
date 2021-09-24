"""
@Author: yanzx
@Date: 2021/5/3 15:38
@Description: 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from .utils import createTree

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            root.right = self.flatten(root.left)




if __name__ == '__main__':
    s = Solution()
    s.flatten()