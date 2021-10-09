"""
@Author: yanzx
@Date: 2021-10-08 16:51:10
@Desc: 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

   1
 2   3
   4  5
     6  7
"""
from utils.binary_tree import TreeNode, floor_print, create_tree


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode):
            if not root:
                return True, 0
            left_bool, left_high = dfs(root.left)
            right_bool, right_high = dfs(root.right)
            if not (left_bool & right_bool):
                return False, 0
            if abs(left_high - right_high) > 1:
                return False, 0
            return True, max(left_high, right_high) + 1,

        res = dfs(root)[0]
        return res


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    s = Solution()
    root = create_tree(nums)
    res = s.isBalanced(root)
    floor_print(root)
    print(res)
