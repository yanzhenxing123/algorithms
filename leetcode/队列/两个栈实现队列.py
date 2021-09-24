"""
@Author: yanzx
@Date: 2020/8/8 18:49
@Description: 简单
"""

class CQueue:

    def __init__(self):
        self.append_stack = []
        self.delete_stack = []


    def appendTail(self, value: int) -> None:
        self.append_stack.append(value)

    def deleteHead(self) -> int:
        if len(self.delete_stack) == 0:
            if len(self.append_stack) == 0:
                return -1
            else:
                while self.append_stack:
                    self.delete_stack.append(self.append_stack.pop())
                return self.delete_stack.pop()
        else:
            return self.delete_stack.pop()