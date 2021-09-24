"""
@Author: yanzx
@Date: 2020/10/19 22:18
@Description:
给你一个由 不同 整数组成的整数数组 arr 和一个整数 k 。

每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。比较 arr[0] 与 arr[1] 的大小，较大的整数将会取得这一回合的胜利并保留在位置 0 ，较小的整数移至数组的末尾。当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。

返回赢得比赛的整数。

题目数据 保证 游戏存在赢家。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-winner-of-an-array-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            """

def f(arr, k):
    # length = len(arr)
    # if length <= k+1:
    #     return max(arr)
    #
    # for i in range(length):
    #     if k == 1:
    #         return arr[i] if arr[i] > arr[i+1] else arr[i+1]
    #
    #     if i == 0:
    #         if arr[0] > max(arr[1: 1+k]):
    #             return arr[0]
    #         for j in range(k):
    #             if arr[0] > arr[1]:
    #                 arr.append(arr[1])
    #                 arr.remove(arr[1])
    #             else:
    #                 arr.append(arr[0])
    #                 arr.remove(arr[0])
    #                 break
    #     else:
    #         if arr[0] > max(arr[1: k]):
    #             return arr[0]
    #
    #         for j in range(k):
    #             if arr[0] > arr[1]:
    #                 arr.append(arr[1])
    #                 arr.remove(arr[1])
    #             else:
    #                 arr.append(arr[0])
    #                 arr.remove(arr[0])
    #                 break


    '''
    :param arr:
    :param k:
    :return:

    遍历一遍即可，因为数组中一定存在winner，所以，遍历一遍后如果没有满足条件的，那么最大值一定为winner
    '''
    res, count = arr[0], 0

    for num in arr[1:]:
        if res > num:
            count += 1
        else:
            res, count = num, 1

        if count == k:
            return res

    return res


if __name__ == '__main__':
    arr = [1,25,35,42,68,70]
    k = 1
    res = f(arr, k)
    print(res)
