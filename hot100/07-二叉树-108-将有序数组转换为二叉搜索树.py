"""
@Time: 2024/4/14 10:15
@Author: yanzx
@Desc:
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
"""
from utils.binary_tree import TreeNode, create_tree, floor_print
from typing import Optional, List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        和二分一起，注意边界点
        :param nums:
        :return:
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[0:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:right + 1])
        return node


if __name__ == '__main__':
    s = Solution()
    res = s.sortedArrayToBST([1, 2, 3, 4, 5])
    print(res)
