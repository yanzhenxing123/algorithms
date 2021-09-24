"""
@Author: yanzx
@Date: 2021/4/7 19:22
@Description:
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        index = inorder.index(preorder[0])
        root = TreeNode(preorder.pop(0))
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        return root


    def print_val(self, root):
        if root:
            self.print_val(root.left)
            self.print_val(root.right)
            print(root.val)



if __name__ == '__main__':
    # 前序遍历
    preorder = [3, 9, 20, 15, 7]
    # 中序遍历
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    res = s.buildTree(preorder, inorder)
    s.print_val(res)
