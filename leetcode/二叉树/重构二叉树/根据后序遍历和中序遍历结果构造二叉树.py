"""
@Author: yanzx
@Date: 2021/5/2 17:26
@Description: 
"""

"""
@Author: yanzx
@Date: 2021/4/29 17:02
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        index = inorder.index(root.val)
        root.right, root.left = self.buildTree(inorder[index+1:], postorder), self.buildTree(inorder[:index], postorder)
        return root


def pre_print_tree(root):
    if root is not None:
        # 先序遍历
        print(root.val)
        pre_print_tree(root.left)
        pre_print_tree(root.right)

if __name__ == '__main__':

    # 中序遍历
    inorder = [9, 3, 15, 20, 7]
    # 后序遍历
    postorder  = [9, 15, 7, 20, 3]
    s = Solution()
    root = s.buildTree(inorder, postorder)
    pre_print_tree(root)