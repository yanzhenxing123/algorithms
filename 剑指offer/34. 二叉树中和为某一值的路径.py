"""
@Author: yanzx
@Date: 2021-09-27 23:14:53
@Desc:
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

[
   [5,4,11,2],
   [5,8,4,5]
]

"""
from utils.binary_tree import TreeNode, List, create_tree, floor_print


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        if not root:
            return res

        def get_sum(path: List[TreeNode]):
            res = 0
            for node in path:
                res = res + node.val
            return res

        def dfs(path: List[TreeNode], root: TreeNode):
            if root:
                path.append(root)
                # 剪枝
                if path and not root.left and not root.right:
                    if get_sum(path) == target:
                        res.append([node.val for node in path])
                dfs(path, root.left)
                dfs(path, root.right)
                path.pop()
        dfs([], root)

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    # nums = [1, 2]
    root = create_tree(nums)
    # floor_print(root)
    res = s.pathSum(root=root, target=22)
    print(res)
