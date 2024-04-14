"""
@Time: 2024/4/14 11:07
@Author: yanzx
@Desc: 
"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        非递归中序遍历到第k个
        :param root:
        :param k:
        :return:
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            root = node.right
