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
        """
        左边和右边一起判断，需要一个新的函数或者方法func(left, right)
        :param root:
        :return:
        """
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
            if left.val != right.val:  # 3. 值不相等则往下走，相等不能返回True，因为还要往下走
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
    
    
    def isSymmetric_2nd(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # 入参需要时left和right
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)
                
        
        

    


if __name__ == '__main__':
    root = create_tree([1, 2, 2, 2, 2, 2, 2])
    s = Solution()
    res = s.isSymmetric(root)
    print(res)
