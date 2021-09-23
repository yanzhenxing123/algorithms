"""
@Author: yanzx
@Date: 2021-09-23 19:19:29
@Desc: 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

   3
   / \
  9  20
    /  \
   15   7

[
  [3],
  [9,20],
  [15,7]
]

"""
from typing import List
from utils.binary_tree import TreeNode, create_tree, floor_print
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append([root])
        while queue:
            nodes = queue.popleft()
            node_vals, node_roots = [], []
            while nodes:
                node = nodes.pop(0)
                node_vals.append(node.val)
                if node.left:
                    node_roots.append(node.left)
                if node.right:
                    node_roots.append(node.right)
            if node_roots:
                queue.append(node_roots)
            if node_vals:
                res.append(node_vals)
        return res


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    root = create_tree(nums)
    s = Solution()
    res = s.levelOrder(root)
    print(res)
