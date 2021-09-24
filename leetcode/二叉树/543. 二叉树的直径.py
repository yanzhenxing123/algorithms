"""
@Author: yanzx
@Date: 2021/5/13 12:36
@Description: 
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_len = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            depth = max(left, right) + 1
            length = left + right + 1
            self.max_len = max(self.max_len, length)
            return depth
        helper(root)
        return self.max_len

if __name__ == '__main__':
    root = TreeNode(3)
    s = Solution()
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    root.left = t2
    root.right = t3
    t3.left = t4
    t3.right = t5
    res = s.diameterOfBinaryTree(root)
    print(res)