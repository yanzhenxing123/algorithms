"""
@Time: 2024/4/15 11:41
@Author: yanzx
@Desc:
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
"""
from utils.binary_tree import TreeNode


class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        两个前序遍历的嵌套
        :param root:
        :param targetSum:
        :return:
        """
        self.res = 0
        self.nodePathSums(root, targetSum)
        return self.res

    def nodePathSums(self, root: TreeNode, targetSum):
        """
        遍历每个节点
        :param root:
        :param targetSum:
        :return:
        """
        if root:
            self.ret = 0
            self.nodePaths(root, 0, targetSum)  # 获取
            self.res += self.ret
            self.nodePathSums(root.left, targetSum)
            self.nodePathSums(root.right, targetSum)

    def nodePaths(self, root: TreeNode, num: int, targetSum: int):
        """
        从当前节点出发有多少个满足条件的
        :return:
        """
        if root:
            num += root.val
            if num == targetSum:
                self.ret += 1
            self.nodePaths(root.left, num, targetSum)
            self.nodePaths(root.right, num, targetSum)

    def pathSum_2(self, root: TreeNode, targetSum: int) -> int:
        """
        比较暴力的解法
        :param root:
        :param targetSum:
        :return:
        """

        self.cur_node_res = 0
        self.res = 0

        def dfs(root):
            if not root:
                return
            self.cur_node_res = 0
            dfs_cur_node(root, 0)
            self.res += self.cur_node_res
            dfs(root.left)
            dfs(root.right)

        def dfs_cur_node(root, cur_total_sum):
            """当前节点为根节点有多少个满足的"""
            if not root:
                return
            cur_total_sum += root.val
            if cur_total_sum == targetSum:
                self.cur_node_res += 1
            dfs_cur_node(root.left, cur_total_sum)
            dfs_cur_node(root.right, cur_total_sum)

        dfs(root)

        return self.res
