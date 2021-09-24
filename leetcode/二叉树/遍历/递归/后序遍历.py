"""
@Author: yanzx
@Date: 2021/5/13 0:14
@Description:
   3
9    20
   15   7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


res = []

a = 100


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        res.append(root.val)


if __name__ == '__main__':
    root = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    root.left = t2
    root.right = t3
    t3.left = t4
    t3.right = t5
    postOrder(root)
    print(res)
