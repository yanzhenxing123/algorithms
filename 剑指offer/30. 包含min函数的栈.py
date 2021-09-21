"""
@Author: yanzx
@Date: 2021-09-21 23:42:40
@Desc:
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
MinStack minStack = new MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.min()   --> 返回 -3.
minStack.pop()
minStack.top()      --> 返回 0.
minStack.min()   --> 返回 -2.

辅助栈 非严格降序
"""

class MinStack:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]



if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    min = minStack.min()  # 返回 - 3.
    print(min)
    minStack.pop()
    minStack.top()  # 返回 0
    minStack.min()  # 返回 -2
