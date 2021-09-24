"""
@Author: yanzx
@Date: 2021/5/3 14:29
@Description: 给你一个已经构造好的最大二叉树，根据654题的描述，这个最大二叉树是对应一个数组的，现在在这个数组后面append一个元素val，然后重新构造一个最大二叉树。
"""
from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if val > root.val:
            return TreeNode(val, root, None)


        parent = root
        cursor = root.right
        while cursor and cursor.val > val:
            parent = cursor
            cursor = cursor.right
        parent.left = TreeNode(val, cursor, None)
        return root
