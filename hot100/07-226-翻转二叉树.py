"""
@Time: 2024/4/13 22:45
@Author: yanzx
@Desc:
      1
   2    3
4    5
"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        先序遍历
        :param root:
        :return:
        """
        if not root:
            return None
        right = root.right
        left = root.left
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.invertTree(root)
    floor_print(res)