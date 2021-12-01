"""
@Author: yanzx
@Date: 2021-12-01 18:25:44
@Desc:给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
         1
      2     3
    4


输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
"""
from typing import List

from utils.binary_tree import TreeNode, create_tree, floor_print


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        广度优先遍历
        :param root:
        :return:
        '''
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
        result = []
        for i in res:
            result.append(i[-1])
        return result


class Solution2:

    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        深度优先：root right left
        :param root:
        :return:
        '''

        res = []

        def dfs(root, depth):
            if root:
                if depth == len(res):
                    res.append(root.val)
                depth += 1
                dfs(root.right, depth)
                dfs(root.left, depth)

        if not root:
            return []
        dfs(root, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    root = create_tree(nums)
    res = s.rightSideView(root)
    print(res)
