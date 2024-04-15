"""
@Time: 2024/4/14 16:08
@Author: yanzx
@Desc: 
"""
from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder是慢慢变化的
        :param preorder:
        :param inorder:
        :return:
        """
        if not inorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        val_index = inorder.index(val)
        root.left = self.buildTree(preorder, inorder[:val_index])
        root.right = self.buildTree(preorder, inorder[val_index + 1:])
        return root


if __name__ == '__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    res = s.buildTree(preorder, inorder)
    floor_print(res)
