"""
@Author: yanzx
@Date: 2021/5/12 16:30
@Description: 173. 二叉搜索树迭代器
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []

    def next(self) -> int:
        while self.root or self.stack:
            while self.root:
                self.stack.append(self.root)
                self.root = self.root.left

            node = self.stack.pop()
            self.root = node.right
            return node.val


    def hasNext(self) -> bool:
        if self.root or self.stack:
            return True
        return False



if __name__ == '__main__':
    root = TreeNode(7)
    node1 = TreeNode(15)
    node2 = TreeNode(20)
    node3 = TreeNode(9)
    node4 = TreeNode(3)

    root.left = node4
    root.right = node1
    node1.left = node3
    node1.right = node2

    iterator = BSTIterator(root)
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.hasNext())
