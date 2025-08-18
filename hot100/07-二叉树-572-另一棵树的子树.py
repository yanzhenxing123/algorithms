"""
@Author: yanzx
@Date: 2025/2/25 16:25
@Description:
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        其实也是两个便利，和路径总和有点像
        :param root:
        :param subRoot:
        :return:
        """
        if not root:
            return not subRoot
        flag = self.isSameTree(root, subRoot)
        return flag or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        if root1.val != root2.val:
            return False

        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
