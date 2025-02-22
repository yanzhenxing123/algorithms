"""
@Author: yanzx
@Date: 2020/11/3 23:15
@Description: 
"""
# Definition for a binary tree node.
from collections import deque

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    root.left = t2
    root.right = t3
    t3.left = t4
    t3.right = t5
    res = s.levelOrder(root)
    print(res)
