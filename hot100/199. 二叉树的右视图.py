"""
@Time: 2024/4/14 11:11
@Author: yanzx
@Desc: 
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        层序遍历
        每一行取最后一个
        :param root:
        :return:
        """
        if not root:
            return []
        q = deque()
        d = {}
        q.append((root, 1))
        while q:
            node, depth = q.popleft()
            if depth not in d:
                d[depth] = [node.val]
            else:
                d[depth].append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        res = []
        for value in d.values():
            res.append(value[-1])
        return res
