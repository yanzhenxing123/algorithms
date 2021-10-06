"""
@Author: yanzx
@Date: 2020/12/7 10:21
@Description: 二叉树的公共祖先 :
              items = [3,5,1,6,2,0,8,None,None,7,4]

            1. 先序遍历打印路径
            2. 后序遍历 DFS
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
        '''
        公共祖先
        :param root:
        :param p:
        :param q:
        '''
        if root.val == p.val or root.val == q.val or root is None:
            return root
        # 两个栈分别用来存储 p  q
        path_p = []
        self.binaryTreePath(root, p, path_p)
        path_q = []
        self.binaryTreePath(root, q, path_q)
        for node_p, node_q in zip(path_p, path_q):
            if node_p is node_q:
                tmp = node_p

        return tmp


    def binaryTreePath(self, root: 'TreeNode', target: 'TreeNode', path: list):
        if not root:
            return False

        path.append(root)

        if root.val == target.val:
            return True

        a = self.binaryTreePath(root.left, target, path)
        b = self.binaryTreePath(root.right, target, path)
        # if a or b:
        #     return True

        path.pop()





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
                if i.left is not None:
                    q.append
                tmp_res.append(i.val)(i.left)
                if i.right is not None:
                    q.append(i.right)
            queue = q
            res.append(tmp_res)
        return res
    return []


if __name__ == '__main__':
    items = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = TreeNode(items[0])
    createTree(root, items)
    # res = levelOrder(root)
    # print(res)
    # print(root.left.right.right.val)
    s = Solution()
    p = TreeNode(5)
    q = TreeNode(1)
    res = s.lowestCommonAncestor(root, p, q)
    print(res.val)
