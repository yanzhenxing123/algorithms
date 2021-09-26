"""
@Author: yanzx
@Date: 2021-09-25 19:50:30
@Desc:

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

     5
    / \
   2   6
  / \
 1   3

输入: [1,3,2,6,5]
输出: true

找到第一个比arr[end]大的，得到该数字的索引为i

判断i之后元素是否比arr[end]大 即arr[i:end-1]
递归 func(arr[start, i-1], arr[i: end-1])
递归结束条件 start>=end 作为true


"""

from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        return self.func(postorder, 0, len(postorder) - 1)

    def func(self, arr, left, right):
        if left >= right:
            return True

        flag = False
        for i in range(left, right):
            if arr[i] > arr[right]:
                flag = True
                break

        if flag:
            for j in range(i, right):
                if arr[j] < arr[right]:
                    return False

        return self.func(arr, left, i - 1) and self.func(arr, i, right-1)


if __name__ == '__main__':
    s = Solution()
    nums = [4, 6, 7, 5]
    res = s.verifyPostorder(nums)
    print(res)
