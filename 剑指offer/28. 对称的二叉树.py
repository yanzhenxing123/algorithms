"""
@Author: yanzx
@Date: 2021-08-11 10:34:10
@Desc: 对称的二叉树

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树[1,2,2,3,4,4,3] 是对称的。

       1
    2    2
  3   4 4  3


示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
"""

from utils.binary_tree import create_tree, TreeNode
from copy import deepcopy


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        copy_root = deepcopy(root)

        # 镜像
        def dfs(root: TreeNode):
            if root is not None:
                dfs(root.left)
                dfs(root.right)
                root.left, root.right = root.right, root.left
        dfs(root)

        # 判断是否为同一颗树
        def is_same_tree(root1: TreeNode, root2: TreeNode):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)

        return is_same_tree(root, copy_root)


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 4, 4, 3]
    root = create_tree(nums)
    s = Solution()
    res = s.isSymmetric(root)
    print(res)