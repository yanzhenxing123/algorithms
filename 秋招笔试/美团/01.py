n, m  = map(int, input().split())


res = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if b <= m:
        cur_min = a
    else:
        cur_min = b
    res += cur_min
print(res)






