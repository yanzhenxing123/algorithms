"""
@Author: yanzx
@Date: 2021-12-01 14:14:17
@Desc: 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""

from typing import List

from utils.binary_tree import TreeNode, create_tree, floor_print


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [[root]]
        res = []
        while queue:
            level = queue.pop(0)
            vals, roots = [], []
            while level:
                root = level.pop(0)
                vals.append(root.val)
                if root.left:
                    roots.append(root.left)
                if root.right:
                    roots.append(root.right)
            res.append(vals)
            if roots:
                queue.append(roots)

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [3, 9, 20, None, None, 15, 7]
    root = create_tree(nums)
    # floor_print(root)
    res = s.levelOrder(root)
    print(res)
