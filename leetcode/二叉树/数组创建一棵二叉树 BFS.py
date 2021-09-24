"""
@Author: yanzx
@Date: 2020/12/7 10:50
@Description: 创建树
"""
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree(root: 'TreeNode', items: list):
    # 构造一个deque
    queue = deque()
    queue.append(root)
    index = 1
    while queue:
        node = queue.popleft()
        if index == len(items):
            break
        if items[index] is not None:
            node.left = TreeNode(items[index])
            queue.append(node.left)
        index += 1

        if items[index] is not None:
            node.right = TreeNode(items[index])
            queue.append(node.right)
        index += 1


if __name__ == '__main__':
    items = [3,5,1,6,2,0,8,None,None,7,4]
    root = TreeNode(items[0])

    createTree(root, items)
    print(root.left.right.right.val)




