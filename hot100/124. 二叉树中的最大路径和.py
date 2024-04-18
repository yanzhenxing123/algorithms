"""
@Time: 2024/4/17 15:26
@Author: yanzx
@Desc:
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

与 543. 二叉树的直径 类似
"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(root: Optional[TreeNode]):
            """
            类似获取 左右孩子路径的最大值
            :param root:
            :return:
            """
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            child_max = max(left, right)
            res = root.val if child_max < 0 else child_max + root.val  # 如果左右都小于0的话就返回自己
            tmp = root.val
            if left > 0:
                tmp += left
            if right > 0:
                tmp += right
            self.ans = max(self.ans, tmp)
            return res

        if not root:
            return 0
        dfs(root)
        return self.ans
