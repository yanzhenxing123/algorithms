"""
@Time: 2024/8/16 18:30
@Author: yanzx
@Desc: 
"""


def heap_adjust(arr, k, n):
    """
    给定二叉树，调整堆
    :param arr: 数组
    :param k: 堆顶元素下标
    :param n: 数组长度
    :return:
    """
    temp = arr[k]  # 堆顶
    i = 2 * k + 1  # 左子树
    while i < n:
        if i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if temp >= arr[i]:
            break
        else:
            arr[k] = arr[i]
            k = i
            i = 2 * k + 1
    arr[k] = temp


def heap_sort(arr, n):
    # 1. 构建大根堆
    for i in range(n // 2 - 1, -1, -1):
        heap_adjust(arr, i, n)
    # 2. 调整堆
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_adjust(arr, 0, i)


def main():
    A = [5, 2, 3, 4, 6, 0, 10, 1, 2, 9]
    n = len(A)
    heap_sort(A, n)
    print(A)


if __name__ == "__main__":
    main()
