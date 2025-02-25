"""
@Time: 2024/4/15 15:18
@Author: yanzx
@Desc: 
"""
from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        后续遍历，且要知道递归终止的条件
        rootwei
        :param root:
        :param p:
        :param q:
        :return:w
        """
        if not root:
            return None
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None

if __name__ == '__main__':
    pass


