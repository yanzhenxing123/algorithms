"""
@Time: 2024/4/14 09:58
@Author: yanzx
@Desc:
103. 二叉树的锯齿形层序遍历
中等
相关标签
premium lock icon
相关企业
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。



示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]

"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        比较简单一次就过
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        count = 1
        while q:
            level_vals = []
            next_q = deque()
            if count % 2 == 1:
                while q:
                    node = q.popleft()
                    level_vals.append(node.val)
                    if node.left:
                        next_q.append(node.left)
                    if node.right:
                        next_q.append(node.right)
            else:
                while q:
                    node = q.pop()
                    level_vals.append(node.val)
                    if node.right:
                        next_q.appendleft(node.right)
                    if node.left:
                        next_q.appendleft(node.left)

            q = next_q
            count += 1
            res.append(level_vals)
        return res


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5])
    s = Solution()
    res = s.levelOrder(root)
    print(res)
