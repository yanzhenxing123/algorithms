"""
@Author: yanzx
@Time: 2025/8/24 23:39 
@Description: 
"""

import random


def estimate_pi(N):
    M = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            M += 1

    pi_per_4 = M / N

    return pi_per_4 * 4


if __name__ == '__main__':
    res = estimate_pi(10 ** 6)
    print(res)
