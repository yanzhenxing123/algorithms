"""
@Time: 2024/4/13 22:52
@Author: yanzx
@Desc: 
"""
from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List
import copy


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 先镜像反转，再看是否一样
        if not root:
            return True

        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]):
            """
            左的左和右的右相同，右的左和左的右相同
            :param left:
            :param right:
            :return:
            """
            if not left and not right:  # 1. 都为空
                return True
            if not (left and right):  # 2. 一个为空
                return False
            if left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(right.left, left.right)

        return dfs(root.left, root.right)


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.isSymmetric(root)
    print(res)
