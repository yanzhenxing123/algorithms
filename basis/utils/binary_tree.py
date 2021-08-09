"""
@Author: yanzx
@Date: 2021-08-07 17:01:45
@Desc: 创建树
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
    root = TreeNode(0)
    queue.append(root)
    for i in range(len(nums)):
        p = queue.popleft()
        p.val = nums[i]
        if i + 1 < len(nums):
            node = TreeNode(0)
            p.left = node
            queue.append(node)
        if i + 1 < len(nums) - 1:
            node = TreeNode(0)
            p.right = node
            queue.append(node)
    return root

class Test(unittest.TestCase):
    def test_create_tree(self):
        """
            3
          4   5
        1  2
        """
        p = create_tree([3,4,5,1,2])

        print(p.val)
        print(p.left.val)
        print(p.left.left.val)
        print(p.right.right.val)
        print(p.right.right.right)







