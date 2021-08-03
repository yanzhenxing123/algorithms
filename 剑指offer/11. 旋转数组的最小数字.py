"""
@Author: yanzx
@Date: 2021/8/2 22:53
@Description:
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

arr[mid] > arr[right] 那么旋转点在mid右边 left = mid + 1
4 5 6 7 1 2 3
0 1 2 3 4 5 6

arr[mid] > arr[right] 那么旋转点在mid左边 right = mid
7 0 1 2 3 4 5 6
0 1 2 3 4 5 6 7

arr[mid] == arr[right] 去重 right -= 1 ★

最后结束条件 left == right

"""


def main(arr):
    if not arr:
        return 0
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[right] > arr[mid]:
            right = mid
        elif arr[right] < arr[mid]:
            left = mid + 1
        else:
            right -= 1
    return right

def main2(arr):
    if not arr:
        return 0
    left, right = 0, len(arr)-1
    while left < right:
        mid = left + (right - left) // 2
        # 左边有序
        if arr[left] < arr[mid]:
            left = mid + 1
        elif arr[left] > arr[mid]:
            right = mid
        else:
            left += 1

    return left




if __name__ == '__main__':
    arr = [7, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    res = main(arr)
    print(res)
