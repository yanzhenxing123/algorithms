def f(gas, cost):
    length = len(gas)
    for i in range(length):
        temp = i
        if gas[i] >= cost[i]:
            x = gas[i] - cost[i]
            for _ in range(length-1):
                if x < 0:
                    break
                if temp >= length-1:
                    temp = -1
                x += gas[temp+1] - cost[temp+1]
                temp += 1
            if x >= 0:
                return i
    return -1

#
# li1 = []
# li2 = []
# gas = input()
# cost = input()
#
# for i in range(len(gas)):
#     if i > 0 and i < (len(gas)-1) and gas[i] != ',':
#         li1.append(int(gas[i]))
#
# for i in range(len(cost)):
#     if i > 0 and i < (len(cost)-1) and gas[i] != ',':
#         li2.append(int(cost[i]))
#
#
#
# print(f(li1, li2))

print(f([4,5,2,6,5,3], [3,2,7,3,2,9]))