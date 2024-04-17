"""
@Time: 2024/4/15 11:41
@Author: yanzx
@Desc:
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
"""
from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.res = 0
        self.nodePathSums(root, targetSum)
        return self.res

    def nodePathSums(self, root: TreeNode, targetSum):
        if root:
            self.ret = 0
            self.nodePaths(root, 0, targetSum)  # 获取
            self.res += self.ret
            self.nodePathSums(root.left, targetSum)
            self.nodePathSums(root.right, targetSum)

    def nodePaths(self, root: TreeNode, num: int, targetSum: int):
        """
        一个节点出发有多少个满足条件的
        :return:
        """
        if root:
            num += root.val
            if num == targetSum:
                self.ret += 1
            self.nodePaths(root.left, num, targetSum)
            self.nodePaths(root.right, num, targetSum)
