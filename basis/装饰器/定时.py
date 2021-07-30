"""
@Author: yanzx
@Date: 2021-07-29 15:59:32
@Desc: 
"""
import time
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("cost time:", end - start)
    return wrapper

@decorator
def func():
    print("I am yanzx")
    time.sleep(1)

if __name__ == '__main__':
    func()
    print(func.__name__)
