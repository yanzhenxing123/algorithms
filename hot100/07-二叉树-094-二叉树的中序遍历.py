"""
@Time: 2024/4/13 22:36
@Author: yanzx
@Desc: 
"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List
import collections


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
    
    def inorderTraversal_2nd(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res

    def inorderTraversal_recur(self, root: Optional[TreeNode]) -> List[int]:
        """
        非递归
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()  # 最小的
            res.append(node.val)
            root = node.right
        return res
    
    def inorderTraversal_recur_2nd(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res 
            
            



if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.inorderTraversal_2(root)
    print(res)
