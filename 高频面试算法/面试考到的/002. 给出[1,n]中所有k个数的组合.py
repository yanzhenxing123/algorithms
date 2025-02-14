"""
@Author: yanzx
@Date: 2025/2/13 14:25
@Description: 小红书一面

"""
#
import copy


def func(n: int, k: int):
    nums = list(range(1, n))
    path = []
    res = []
    print(nums)
    dfs(nums, path, k, 0, res)
    print(res)
    pass


def dfs(nums: list, path: list, k: int, index: int, res: list):
    if len(path) == k:
        res.append(copy.deepcopy(path))
        return

    for i in range(index, len(nums)):
        path.append(nums[i])
        dfs(nums, path, k, i + 1, res)
        path.pop()


if __name__ == '__main__':
    func(8, 3)
