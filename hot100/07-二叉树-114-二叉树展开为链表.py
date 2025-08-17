"""
@Time: 2024/4/14 11:19
@Author: yanzx
@Desc:
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

"""
from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        先遍历存储，然后修改右指针

        """
        if not root:
            return None
        nodes = []

        def preorder(root: Optional[TreeNode]):
            if root:
                nodes.append(root)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]


class Solution_2:
    def __init__(self):
        self.preNode = None

    def flatten(self, root: TreeNode) -> None:
        """
        不使用额外的空间，O(h), h为树的深度
        先序遍历：中 左 右
        反先序遍历: 右 左 中

        这时候是先序遍历的反过来，第一个节点就是先序遍历的最后一个节点；
        :param root:
        :return:
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.preNode
        self.preNode = root
