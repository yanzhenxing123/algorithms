"""
@Author: yanzx
@Date: 2021/5/2 16:20
@Description: 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root



def get_tree():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    return root

def i_print_tree(root):
    if root is not None:
        print(root.val)
        i_print_tree(root.left)
        i_print_tree(root.right)

if __name__ == '__main__':
    root = get_tree()
    i_print_tree(i_print_tree(root))
    print("*" * 100)
    s = Solution()
    root = s.invertTree(root=root)
    i_print_tree(root)


