"""
@Author: yanzx
@Date: 2020/8/3 15:29
@Description: 
"""
def f(s: str):
    max_length = 0
    pool = []
    for i in s:
        if i in pool:
            index = pool.index(i)
            pool = pool[index+1:]
        pool.append(i)
        max_length = max(max_length, len(pool))

    return max_length