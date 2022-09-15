"""
@Author: yanzx
@Date: 2021/12/11 15:20
@Description:
"""

arr = [0, 0, 0, 1]
arr.extend(list([0 for i in range(100)]))
for i in range(4, 100):
    arr[i] = (arr[i-1] + 3 * arr[i-2] - 2 * arr[i-3] - arr[i-4]) % 1000000007


print(arr)
for i in arr:
    print(i)

