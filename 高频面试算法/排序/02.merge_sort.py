"""
@Author: yanzx
@Date: 2021-09-28 21:26:03
@Desc: 归并排序
"""


def merge(left_arr, right_arr):
    left_index, right_index, merge_arr = 0, 0, list()
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    return merge_arr + left_arr[left_index:] + right_arr[right_index:]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left_arr = merge_sort(arr[:len(arr) // 2])
    right_arr = merge_sort(arr[len(arr) // 2:])
    return merge(left_arr, right_arr)


if __name__ == '__main__':
    arr = []
    print(merge_sort(arr))
