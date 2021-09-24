"""
@Author: yanzx
@Date: 2021/5/14 8:57
@Description: 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import namedtuple

class Solution:
    # namedtuple(Result, ())

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            pass




from .utils import create_demo_tree

if __name__ == '__main__':
    root = create_demo_tree()

    s = Solution()
    res = s.subtreeWithAllDeepest(root)
    print(res)


