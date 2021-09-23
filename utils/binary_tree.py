"""
@Author: yanzx
@Date: 2021-08-07 17:01:45
@Desc: 创建树

层序遍历创建的是一颗满二叉树，满二叉树的节点索引的对应关系为

left_i = root_i * 2 + 1
right_i = root_i * 2 + 2

"""
import unittest
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_tree(nums: List[int]) -> TreeNode:
    """
    层序遍历来创建一棵树
    :param nums:
    :return:
    """
    if not nums:
        return None
    queue = deque()
    root = TreeNode(nums[0])
    index = 1
    queue.append(root)
    while queue:
        node = queue.popleft()
        if index >= len(nums):
            break
        if nums[index] is not None:
            left_node = TreeNode(nums[index])
            node.left = left_node
            queue.append(left_node)
        index += 1
        if index >= len(nums):
            break
        if nums[index] is not None:
            right_node = TreeNode(nums[index])
            node.right = right_node
            queue.append(right_node)
        index += 1
    return root


def floor_print(root: TreeNode):
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


class Test(unittest.TestCase):
    def test_create_tree(self):
        """
                0
              1   2
            3  4 5 6
          7  8 9 10

               3
            4     5
        1    2   N    N

        """
        root = create_tree([3, 4, 5, 1, 2])
        print(root)

    def test_floor_print_tree(self):
        root = create_tree([3, 4, 5, 1, 2])
        floor_print(root)
