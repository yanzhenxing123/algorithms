"""
@Author: yanzx
@Date: 2021/12/11 20:33
@Description:
"""

x1 = 1
x2 = -1.532089
x3 = -0.347296
x4 = 1.879385
#
# for i in range(4):
#     print(x1 ** 2, ",", x2 ** i, ",", x3 ** i, ",", x4 ** i)

y1 = -0.33333350
y2 = -0.09770943
y3 = 0.28134325
y4 = 0.14969968


def get_an(n):
    an = y1 * x1 ** n + y2 * x2 ** n + y3 * x3 ** n + y4 * x4 ** n
    return round(an) % 1000000007


# n = int(input())
n  = 100
for i in range(n):
    # j = int(input())
    print(get_an(i))


