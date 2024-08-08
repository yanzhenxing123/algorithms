"""
@Time: 2024/8/7 15:33
@Author: yanzx
@Desc:

"""

from utils.binary_tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        后序遍历，从叶子结点向上返回
        1. 如果叶子结点为p或者q，则返回自己，否则返回None
        2. 如果自己左右孩子都不为None，返回自己
        3. 如果自己左孩子或者右孩子不为None，则返回左孩子或右孩子
        4. 否则 返回None
        :param root:
        :param p:
        :param q:
        :return:
        """

        def dfs(root: 'TreeNode'):
            if not root:
                return None
            if root is p or root is q:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            if (left and right):
                return root
            if left:
                return left
            if right:
                return right
            return None

        return dfs(root)
