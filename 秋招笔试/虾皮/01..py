# """
# @Author: yanzx
# @Time: 2025/8/20 16:32
# @Description:
# """
#
# import json
#
#
#
# string = "nums = [1,5,9,1,5,9], k = 2, t =  3"  # 字符串转化为正常的变量
#
# # string = input().strip()
#
# # left, right = string.index('['), string.index(']')
# # k_index_left = string.index('k =')
# # k_index_right = string.index(', t')
# # t_index_left = string.index('t =')
# #
# # nums = json.loads(string[left:right+1])
# # k = int(string[k_index_left+3:k_index_right])
# # t = int(string[t_index_left+3:])
# # print(k)
# # print(t)
#
# try:
#     for part in string.split(", "):
#         exec(part)
# except:
#     print("false")
#     import sys
#     sys.exit(0)
#
#
#
# def check(nums, k, t):
#     if not nums:
#         return "false"
#     length = len(nums)
#     for i in range(length):
#         for j in range(i, length):
#             if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
#                 return "true"
#
#     return "false"
#
# res = check(nums, k, t)
# print(res)
#
#
# # import bisect
# # def check_2(nums, k, t):
# #     if t < 0 or k > 0:
# #         return False
# #
# #     window = []
# #     for i, num in enumerate(nums):
# #         idx = bisect.bisect_left(window, num-t)
# #         if idx < len(window) and abs(window[idx] - num) <=t:
# #             return True
# #         bisect.insort(window, num)
# #         if len(window) > k:
# #             left_num = num[i-k]
# #             index = bisect.bisect_left(window, left_num)
# #             if index < len(window) and window[index] == left_num:
# #                 window.pop(index)
# #
# #         return False
# #
# # res = check(nums, k, t)
# # print(res)

# import json


# string = "{nums = [1,5,9,1,5,9], k = 2, t =  3}"  # 字符串转化为正常的变量


# # string = "nums = [1,5,9,1,5,9], k = 2, t =  3"  # 字符串转化为正常的变量


# # for part in string.split(", "):
# #     exec(part)

# left, right = string.index('['), string.index(']')
# k = string.split('k')[1].split('t')[0].replace("=", "").replace(',', "")
# k = int(k)
# print(k)



def check(nums, k, t):
    if not nums:
        return "true"
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                return "true"
    return "false"


if __name__ == '__main__':
    nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3
    res = check(nums, k, t)
    print(res)
