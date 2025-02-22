"""
@Time: 2024/4/13 22:36
@Author: yanzx
@Desc: 
"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node: Optional[TreeNode]):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        return res


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.inorderTraversal(root)
    print(res)
