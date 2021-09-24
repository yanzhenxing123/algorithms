"""
@Author: yanzx
@Date: 2021/5/13 10:23
@Description: 559. N 叉树的最大深度
"""
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        queue = deque()
        queue.append((root, 1))
        max_depth = 1
        while deque:
            node, depth = queue.popleft()
            max_depth = max(depth, max_depth)
            if node.children:
                for child in node.children:
                    if child:
                        queue.append((child, depth + 1))
            return max_depth





if __name__ == '__main__':
    s = Solution()