"""
@Author: yanzx
@Date: 2021/5/2 23:00
@Description: 
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 二分
        def helper(left, right):
            if left >= right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.right, root.left =  helper(mid+1, right), helper(left, mid)
            return root

        return helper(0, len(nums))


def in_print_tree(root):
    if root is not None:
        # 中序遍历
        in_print_tree(root.left)
        print(root.val)
        in_print_tree(root.right)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    root = s.sortedArrayToBST(nums)
    in_print_tree(root)
