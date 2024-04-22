"""
@Time: 2024/4/21 15:59
@Author: yanzx
@Desc: 
"""


from typing import Optional
from utils import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left:
            return right + 1
        if not right:
            return left + 1
        return min(left, right) + 1
