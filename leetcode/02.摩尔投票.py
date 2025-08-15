"""
@Author: yanzx
@Date: 2020/10/19 17:17
@Description: 摩尔投票
"""

def f(nums):

    # # 初始化count和major
    # major, count = None, 0
    # for x in nums:
    #     if count == 0:
    #         major, count = x, 1
    #     elif x == major:
    #         count = count + 1
    #     else:
    #         count = count - 1
    #
    # count = 0
    #
    # # 检查 相当于count = nums.count(major)
    # for i in nums:
    #     if major == i:
    #         count += 1
    # if count > int(len(nums) / 2):
    #     return major
    # else:
    #     return -1

    count_dict = {}
    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    for key, value in count_dict.items():
        if value == max(count_dict.values()):
            return key

    


if __name__ == '__main__':
    nums = [1, 2, 3,3,3, 4]
    res = f(nums)
    print(res)