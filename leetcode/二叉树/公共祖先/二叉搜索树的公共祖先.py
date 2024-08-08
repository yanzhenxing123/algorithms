"""
@Author: yanzx
@Date: 2020/12/7 10:21
@Description: 二叉树搜索树的公共祖先
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode:
        if root.val == q.val:
            return root
        elif root.val == q.val:
            return root

        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return w

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        while res:
            if p.val < res.val and q.val < res.val:
                res = res.left
            elif p.val > res.val and q.val > res.val:
                res  = res.right
            else:
                break
        return res



def createTree(root: 'TreeNode', items: list):
    '''
    创建树
    :param root:
    :param items:
    :return:
    '''
    # 构造一个deque
    queue = deque()
    queue.append(root)
    index = 1
    while queue:
        node = queue.popleft()
        if index == len(items):
            break
        if items[index] is not None:
            node.left = TreeNode(items[index])
            queue.append(node.left)
        index += 1

        if items[index] is not None:
            node.right = TreeNode(items[index])
            queue.append(node.right)
        index += 1


def levelOrder(root: TreeNode):
    '''
    层序遍历
    :param root:
    :return:
    '''
    if root:
        queue = []
        queue.append(root)
        res = []
        while queue:
            q = []
            tmp_res = []
            for i in queue:
                tmp_res.append(i.val)
                if i.left is not None:
                    q.append(i.left)
                if i.right is not None:
                    q.append(i.right)
            queue = q
            res.append(tmp_res)
        return res
    return []


if __name__ == '__main__':
    items = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = TreeNode(items[0])
    createTree(root, items)
    # res = levelOrder(root)
    # print(res)
    # print(root.left.right.right.val)
    s = Solution()
    p = TreeNode(2)
    q = TreeNode(8)
    res = s.lowestCommonAncestor(root, p, q)
    print(res.val)
