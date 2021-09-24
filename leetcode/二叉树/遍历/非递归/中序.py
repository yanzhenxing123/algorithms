"""
@Author: yanzx
@Date: 2021/5/12 16:45
@Description: 
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return []
    res = []
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        if stack:
            node = stack.pop()
            res.append(node.val)
            root = node.right

    return res


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
    res = levelOrder(root)
    print(res)