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
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            root.val = 1 + max(dfs(root.left), (dfs(root.right)))
            return root.val

        dfs(root)
        self.res = 0

        self.dfs2(root)
        return self.res

    def dfs2(self, root: Optional[TreeNode]):
        if root:
            if root.left and root.right:
                depth = root.left.val + root.right.val
            elif root.left:
                depth = root.left.val
            elif root.right:
                depth = root.right.val
            else:
                depth = 0
            if depth > self.res:
                self.res = depth
            self.dfs2(root.left)
            self.dfs2(root.right)


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.diameterOfBinaryTree(root)
    print(res)
