"""
@Author: yanzx
@Date: 2021/5/13 10:27
@Description: 
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     left = self.maxDepth(root.left)
    #     right = self.maxDepth(root.right)
    #     return max(left, right) + 1

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        max_depth = 1
        while queue:
            node, depth = queue.popleft()
            max_depth = max(depth, max_depth)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return max_depth

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
    res = s.maxDepth(root)
    print(res)
