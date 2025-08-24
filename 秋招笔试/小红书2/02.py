"""
@Time: 2025/8/24 19:24
@Author: yanzx
@Description: 


5 3
1 2 2 5 6
4
2
1

=>> 3 4 5

"""

MAX_SCORE = 5 * 10 ** 5

def solve():
    n, m = map(int, input().split())
    a =  list(map(int, input().split()))
    freq = [0] * (MAX_SCORE + 1)
    for score in a:
        freq[score] += 1
    divisors_count = [0] * (MAX_SCORE + 1)
    for k in range(1, MAX_SCORE + 1):
        if freq[k] > 0:
            for j in range(k, MAX_SCORE + 1, k):
                divisors_count[j] += freq[k]
    muliples_count = [0] * (MAX_SCORE + 1)
    for k in range(1, MAX_SCORE + 1):
        for j in range(k, MAX_SCORE + 1, k):
            muliples_count[k] += freq[j]

    results = []
    for _ in range(m):
        x = int(input())
        cur_compatiples = muliples_count[x] + divisors_count[x]
        if freq[x] > 0:
            cur_compatiples -= freq[x]
        results.append(cur_compatiples)
    
    for res in results:
        print(res)

solve()
        
    


