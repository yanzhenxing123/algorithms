"""
@Author: yanzx
@Date: 2021-08-11 10:17:04
@Desc: 二叉树的镜像

后序遍历 交换节点

"""
from basis.utils.binary_tree import create_tree, TreeNode, floor_print

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            if root is not None:
                self.mirrorTree(root.left)
                self.mirrorTree(root.right)
                root.left, root.right = root.right, root.left
        dfs(root)
        return root

if __name__ == '__main__':
    nums = [4, 2, 7, 1, 3, 6, 9]
    root = create_tree(nums)
    floor_print(root)
    s = Solution()
    new_root = s.mirrorTree(root)
    print("*" * 20)

    floor_print(new_root)
