"""
@Time: 2024/4/14 10:28
@Author: yanzx
@Desc:
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左
子树
只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""
from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        中序遍历后，判断有序，二叉搜索树中不存在相同元素
        :param root:
        :return:
        """
        nums = []

        def inorder(root: Optional[TreeNode]):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)

        inorder(root)
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.isValidBST(root)
    print(res)
