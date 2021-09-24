"""
@Author: yanzx
@Date: 2021/5/3 14:29
@Description: 
"""
from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_num = max(nums)
        index = nums.index(max_num)
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root

def levelOrder(root: TreeNode) -> List[int]:
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
    s = Solution()
    nums = [3,2,1,6,0,5]
    root = s.constructMaximumBinaryTree(nums=nums)
    res = levelOrder(root)
    print(res)
