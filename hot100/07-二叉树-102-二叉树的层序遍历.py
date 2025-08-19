"""
@Time: 2024/4/14 09:58
@Author: yanzx
@Desc:
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。


"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        pass
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            vals = []
            next_queue = deque()
            for node in queue:
                vals.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            res.append(vals)
            queue = next_queue
        return res

    def levelOrder_2nd(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            next_queue = deque()
            vals = []
            for node in q:
                vals.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            res.append(vals)
            q = next_queue

        return res
    
    def levelOrder_3rd(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    




if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.levelOrder(root)
    print(res)
