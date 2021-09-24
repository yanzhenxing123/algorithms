"""
@Author: yanzx
@Date: 2021/5/2 17:38
@Description: 
"""


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def dfs(pre, post):
            if not pre:
                return None
            # 数组长度为1时，直接返回即可
            if len(pre) == 1:
                return TreeNode(pre[0])
            # 根据前序数组的第一个元素，创建根节点
            root = TreeNode(pre[0])
            # 根据前序数组第二个元素，确定后序数组左子树范围
            left_count = post.index(pre[1])+1
            # 递归执行前序数组左边、后序数组左边
            root.left = dfs(pre[1:left_count+1],post[:left_count])
            # 递归执行前序数组右边、后序数组右边
            root.right = dfs(pre[left_count+1:],post[left_count:-1])
            # 返回根节点
            return root
        return dfs(pre, post)

def in_print_tree(root):
    if root is not None:
        # 中序遍历
        in_print_tree(root.left)
        print(root.val)
        in_print_tree(root.right)


if __name__ == '__main__':
    # 前序遍历
    preorder = [1, 2, 4, 5, 3, 6, 7]
    # 后序遍历
    postorder = [4, 5, 2, 6, 7, 3, 1]
    s = Solution()
    root = s.constructFromPrePost(preorder, postorder)
    in_print_tree(root)

