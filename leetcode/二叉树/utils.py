"""
@Author: yanzx
@Date: 2021/5/13 17:47
@Description: 
"""
"""
@Author: yanzx
@Date: 2020/12/7 14:50
@Description: 
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree(root: 'TreeNode', items: list):
    '''
    创建树
    :param root:
    :param items:
    :return:
    '''
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

def create_demo_tree():
    root = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    root.left = t2
    root.right = t3
    t3.left = t4
    t3.right = t5
    return root
