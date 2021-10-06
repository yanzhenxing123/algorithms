"""
@Author: yanzx
@Date: 2021-10-06 12:50:33
@Desc:
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

解题思路：后序遍历

"""

from utils.binary_tree import TreeNode, create_tree, floor_print


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is not None:
            return left

        if right is not None:
            return right
        else:
            return None


if __name__ == '__main__':
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_tree(nums)
    s = Solution()
    res = s.lowestCommonAncestor(root, TreeNode(5), TreeNode(4))
    print(res.val)
