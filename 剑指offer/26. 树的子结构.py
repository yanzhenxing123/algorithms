"""
@Author: yanzx
@Date: 2021-08-05 09:46:31
@Desc: 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False

        # 左右递归
        def hashSubStructure(A: TreeNode, B: TreeNode) -> bool:
            if not B:
                return True
            if not A:
                return False
            if A.val == B.val:
                return hashSubStructure(A.left, B.left) and hashSubStructure(A.right, B.right)
            return False

        return hashSubStructure(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


if __name__ == '__main__':
    s = Solution()

    # s.isSubStructure(A, B)
