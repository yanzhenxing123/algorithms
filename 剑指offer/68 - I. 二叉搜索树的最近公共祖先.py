"""
@Author: yanzx
@Date: 2021-10-06 12:27:30
@Desc:

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：
“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
"""

from utils.binary_tree import TreeNode, create_tree, floor_print


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == root.val or q.val == root.val:
            return root
        if root.val > q.val and root.val < p.val:
            return root
        if root.val < q.val and root.val > p.val:
            return root

        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return None


if __name__ == '__main__':
    s = Solution()
    nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = create_tree(nums)
    p = TreeNode(2)
    q = TreeNode(4)
    res = s.lowestCommonAncestor(root, p, q)
    print(res.val)
