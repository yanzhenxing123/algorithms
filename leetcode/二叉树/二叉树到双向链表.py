"""
@Author: yanzx
@Date: 2020/12/19 21:46
@Description: 
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.pre = None
        self.zhongxuBianli(root)
        return self.head

    def zhongxuBianli(self, curr: 'Node'):
        if not curr:
            return
        self.zhongxuBianli(curr.left)
        if not self.pre:
            self.head = self.pre = curr
        else:
            self.pre.right = curr
            curr.left = self.pre
            self.pre = curr

        self.zhongxuBianli(curr.right)


if __name__ == '__main__':
    s = Solution()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    res = s.treeToDoublyList(None)

