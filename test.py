"""
@Author: yanzx
@Date: 2021-09-27 22:55:24
@Desc: 
"""
import random
import unittest
from typing import List


class MyTest(unittest.TestCase):
    def test_merge_sort(self):
        def merge_sort(arr: List[int]):
            if len(arr) <= 1:
                return arr
            left_arr = merge_sort(arr[:len(arr) // 2])
            right_arr = merge_sort(arr[len(arr) // 2:])
            return merge(left_arr, right_arr)

        def merge(left_arr, right_arr):
            left_index, right_index, res = 0, 0, []
            while left_index < len(left_arr) and right_index < len(right_arr):
                if left_arr[left_index] < right_arr[right_index]:
                    res.append(left_arr[left_index])
                    left_index += 1
                else:
                    res.append(right_arr[right_index])
                    right_index += 1
            return res + left_arr[left_index:] + right_arr[right_index:]
        nums = [random.randint(1, 1000) for _ in range(100)]
        res = merge_sort(nums)
        print(res)
