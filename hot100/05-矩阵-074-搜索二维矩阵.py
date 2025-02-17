"""
@Time: 2024/4/25 23:29
@Author: yanzx
@Desc: 
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    s = Solution()
    res = s.searchMatrix(matrix, target=16)
    print(res)
