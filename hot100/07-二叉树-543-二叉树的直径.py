"""
@Time: 2024/4/13 23:15
@Author: yanzx
@Desc:
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。
"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        左边深度加右边深度就是当前节点的直径
        :param root:
        :return:
        """
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            diameter = left + right
            self.res = max(self.res, diameter)
            return max(right, right)

        dfs(root)
        return self.res


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.diameterOfBinaryTree(root)
    print(res)
