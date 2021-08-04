"""
全排列
"""

from typing import List


def permute(arr: List[int]):
    res = []

    def dfs(path):
        if len(path) == len(arr):
            res.append(path.copy())
            return

        for i in range(len(arr)):
            if arr[i] in path:
                continue
            path.append(arr[i])
            dfs(path)
            path.pop()

    dfs([])
    return res


if __name__ == '__main__':
    res = permute([1, 2, 3, 4])
    print(res)
