import json
import sys
string = "nums = [1,0,1,1], k = 1, t =  2"  # 字符串转化为正常的变量

# string = input()
if not string or 'k' not in string or 't' not in 'string' or '=' not in string or ',' not in string:
    print('false')
    sys.exit(0)

for part in string.split(", "):
    exec(part)

# left, right = string.index('['), string.index(']')
# nums = json.loads(string[left:right+1])

# k = string.split('k')[1].split('t')[0].replace("=", "").replace(',', "")
# k = int(k)


def check(nums, k, t):
    if not nums:
        return "false"
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                return "true"
    return "false"
res = check(nums, k, t)
print(res)