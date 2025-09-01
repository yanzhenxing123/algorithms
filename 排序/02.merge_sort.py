"""
@Author: yanzx
@Date: 2021-09-28 21:26:03
@Desc: 归并排序
"""


def merge_sort(alist):
    """
    递归终止的条件：有序，即 数组长度为0或1
    先分再和
    :param alist:
    :return:
    """
    if len(alist) <= 1:
        return alist
    # 二分分解
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    # 合并
    return merge(left, right)


def merge(left, right):
    """
    合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组
    :param left:
    :param right:
    :return:
    """
    # left与right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_alist = merge_sort(alist)
    print(sorted_alist)
