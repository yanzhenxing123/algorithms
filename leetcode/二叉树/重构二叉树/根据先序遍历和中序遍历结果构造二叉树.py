"""
@Author: yanzx
@Date: 2021/5/2 17:02
@Description:  根据先序遍历和中序遍历结果构造二叉树
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        index = inorder.index(preorder[0])
        root = TreeNode(preorder.pop(0))
        root.left, root.right = self.buildTree(preorder, inorder[:index]), self.buildTree(preorder, inorder[index+1:])
        return root


def post_print_tree(root):
    if root is not None:
        # 后序遍历
        post_print_tree(root.left)
        post_print_tree(root.right)
        print(root.val)


if __name__ == '__main__':
    # 前序遍历
    preorder = [3, 9, 20, 15, 7]
    # 中序遍历
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    root = s.buildTree(preorder, inorder)
    post_print_tree(root)

