"""
@Time: 2024/4/14 16:08
@Author: yanzx
@Desc: preorder 和 inorder 均 无重复 元素
使用index获取单签
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

"""
from typing import Optional, List

from utils.binary_tree import TreeNode, floor_print


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder是慢慢变化的，这个不是很会写
        就是一个先序遍历
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

    def buildTree_2nd(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        # 根节点是preorder中的第一个
        val = preorder.pop(0)
        root = TreeNode(val)
        val_index = inorder.index(val)
        root.left = self.buildTree_2nd(preorder, inorder[:val_index])
        root.right = self.buildTree_2nd(preorder, inorder[val_index + 1:])
        return root


if __name__ == '__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    res = s.buildTree(preorder, inorder)
    floor_print(res)
