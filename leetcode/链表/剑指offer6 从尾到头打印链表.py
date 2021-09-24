"""
@Author: yanzx
@Date: 2021/4/7 0:39
@Description: 
"""
from typing import List


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        def wrapper(head: ListNode):
            if head is not None:
                if head.next is not None:
                    wrapper(head.next)
                res.append(head.val)
        wrapper(head)
        return res



if __name__ == '__main__':
    head = ListNode(0)
    p = head
    for i in range(1, 10):
        p.next = ListNode(i)
        p = p.next

    s = Solution()
    res = s.reversePrint(head)
    print(res)