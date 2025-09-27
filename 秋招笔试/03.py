import math

t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    balance = 0
    min_balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        if balance < min_balance:
            min_balance = balance

    swaps = math.ceil(abs(min_balance) / 2)
    results.append(swaps)

for res in results:
    print(res)