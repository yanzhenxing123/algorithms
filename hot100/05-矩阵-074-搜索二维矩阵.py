"""
@Time: 2024/4/25 23:29
@Author: yanzx
@Desc: 



给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

 

示例 1：


输入：matrix = [ [1,3,5,7],
                [10,11,16,20],
                [23,30,34,60]], target = 3
输出：true

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        先找到targe在哪一行，然后用二分查找这一行
        Args:
            matrix (List[List[int]]): _description_
            target (int): _description_

        Returns:
            bool: _description_
        """
        def binary_search(arr, target):
            left, right = 0, len(arr)
            while left <= right:
                mid = (left + right) // 2
                if target == arr[mid]:
                    return True
                elif target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:  # 小于最小值
                bottom = row - 1
            elif target >= matrix[row][0] and target <= matrix[row][-1]:
                print(f'row mid:{row}')
                return binary_search(matrix[row], target)  # 在这个区间当中
            else:  # 大于最大值
                top = row + 1
        return False

    def searchMatrix_2nd(self, matrix: List[List[int]], target: int) -> bool:
        pass

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    s = Solution()
    res = s.searchMatrix(matrix, target=16)
    print(res)
