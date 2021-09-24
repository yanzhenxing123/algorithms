"""
@Author: yanzx
@Date: 2020/10/20 16:08
@Description: 简单的回溯问题
"""
res = []

def backtrack(path, nums):
    if len(path) == 3:
        if sum(path) == 0:
            new_path = sorted(path)
            if not new_path in res:
                res.append(new_path)
            return
        return

    for i in range(len(nums)):
        # 复制操作
        new_nums = nums.copy()
        new_nums.pop(i)
        path.append(nums[i])
        backtrack(path, new_nums)
        path.pop()


if __name__ == '__main__':
    backtrack([], nums=[12,5,-12,4,-11,11,2,7,2,-5,-14,-3,-3,3,2,-10,9,-15,2,14,-3,-15,-3,-14,-1,-7,11,-4,-11,12,-15,-14,2,10,-2,-1,6,7,13,-15,-13,6,-10,-9,-14,7,-12,3,-1,5,2,11,6,14,12,-10,14,0,-7,11,-10,-7,4,-1,-12,-13,13,1,9,3,1,3,-5,6,9,-4,-2,5,14,12,-5,-6,1,8,-15,-10,5,-15,-2,5,3,3,13,-8,-13,8,-5,8,-6,11,-12,3,0,-2,-6,-14,2,0,6,1,-11,9,2,-3,-6,3,3,-15,-5,-14,5,13,-4,-4,-10,-10,11])
    print(res)