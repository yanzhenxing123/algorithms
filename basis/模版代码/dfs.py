"""
全排列
"""

from typing import List


def permute(arr: List[int]):
    '''
    没有相同的元素可以这样做
    但是有相同的元素就不可以这样做 要使用 permute2
    :param arr:
    :return:
    '''
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


def permute2(arr: List[int]):
    res = []
    visited = [False for _ in range(len(arr))]

    def dfs(path):
        if len(arr) == len(path):
            res.append(path.copy())

            return

        for i in range(len(arr)):
            if visited[i]:
                continue
            path.append(arr[i])
            visited[i] = True
            dfs(path)
            path.pop()
            visited[i] = False
    dfs([])
    return res



if __name__ == '__main__':
    res = permute2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(res)
