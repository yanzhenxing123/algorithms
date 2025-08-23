import math


def count_special_numbers(n, x, y):
    special = set()
    
    special.update(range(x, n + 1, x))
    special.update(range(y, n + 1, y))
    
    # x 因子
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if i <= n:
                special.add(i)
            if x // i <= n:
                special.add(x // i)
    
    # y 因子
    for i in range(1, int(math.sqrt(y)) + 1):
        if y % i == 0:
            if i <= n:
                special.add(i)
            if y // i <= n:
                special.add(y // i)
    
    return len(special)

n, x, y = map(int, input().split())
res = count_special_numbers(n, x, y)
print(res)