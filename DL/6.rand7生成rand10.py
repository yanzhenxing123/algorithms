"""
@Author: yanzx
@Time: 2025/8/24 23:47 
@Description: 
"""

import random

def rand7():
    return random.randint(1, 7)

def rand10():

    while True:
        a = rand7() - 1
        b = rand7() - 1

        c = a * 7 + b

        if c < 40:
            return c // 4 + 1


def rand100():
    while True:
        a = rand7() - 1
        b = rand7() - 1
        c = a * 7 * 7 + b
        if c < 300:
            return c // 3 + 1


if __name__ == '__main__':
    res = rand100()
    print(res)