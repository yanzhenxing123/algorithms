"""
@Author: yanzx
@Date: 2021-09-25 10:15:06
@Desc:
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

[
  [3],
  [20,9],
  [15,7]
]
"""


from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import List
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not nums:
            return []

        stack1, stack2 = [], []
        stack1.append(root)
        res = []
        while stack1 or stack2:
            res_stack = []
            while stack1:
                node = stack1.pop()
                print(node.val)
                res_stack.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            if res_stack:
                res.append(res_stack.copy())
            res_stack.clear()
            while stack2:
                node = stack2.pop()
                res_stack.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
            if res_stack:
                res.append(res_stack.copy())
            res_stack.clear()
        return res



if __name__ == '__main__':
    s = Solution()
    nums = [3, 9, 20, None, None, 15, 7]
    root = create_tree(nums)
    res = s.levelOrder(root)
    print(res)