"""
@Author: yanzx
@Date: 2021/5/12 23:47
@Description: 
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        if not root:
            return []
        stack, res = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                for c in node.children:
                    if c:
                        stack.append(c)
        return res[::-1]

if __name__ == '__main__':
    root = Node(3)
    t2 = Node(9)
    t3 = Node(20)
    t4 = Node(15)
    t5 = Node(7)
    root.children = [t2, t3, t4, t5]
    s = Solution()
    res = s.postorder(root)
    print(res)
