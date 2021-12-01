"""
@Author: yanzx
@Date: 2021-12-01 18:19:38
@Desc: 94. 二叉树的中序遍历

左 中 右

"""
from typing import List

from utils.binary_tree import TreeNode, create_tree, floor_print


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == '__main__':
    s = Solution()
    nums = [1, None, 2, 3]
    root = create_tree(nums)
    res = s.inorderTraversal(root=root)
    print(res)
