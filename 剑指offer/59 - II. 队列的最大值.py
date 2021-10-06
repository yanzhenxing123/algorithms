"""
@Author: yanzx
@Date: 2021-10-06 16:53:06
@Desc:
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value需要返回 -1

解题思路：
queue保存原始元素

deque保存一个降序的队列


"""

from collections import deque


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

class MaxQueue:
    def __init__(self):
        self.queue = []
        self.deque = deque()

    def max_value(self) -> int:
        if not self.deque:
            return -1
        return self.deque[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)

        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)


    def pop_front(self) -> int:
        if not self.queue:
            return -1
        val = self.queue.pop(0)
        if self.deque[0] == val:
            self.deque.popleft()
        return val


if __name__ == '__main__':
    pass
