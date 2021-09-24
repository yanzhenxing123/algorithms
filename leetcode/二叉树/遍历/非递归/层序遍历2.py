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
    def levelOrder(self, root: TreeNode) -> List[list]:
        if root:
            queue = []
            queue.append(root)
            res = []
            while queue:
                q = []
                tmp_res = []
                for i in queue:
                    tmp_res.append(i.val)
                    if i.left is not None:
                        q.append(i.left)
                    if i.right is not None:
                        q.append(i.right)

                queue = q
                res.append(tmp_res)

            return res
        return []


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
