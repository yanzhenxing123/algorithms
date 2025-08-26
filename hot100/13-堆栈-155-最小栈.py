"""
@Time: 2024/4/27 09:44
@Author: yanzx
@Desc: 
"""


class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []  # 存储最小的相同的元素

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.data.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
