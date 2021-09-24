"""
@Author: yanzx
@Date: 2020/8/8 18:52
@Description: 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        index = 1
        pos = head
        while pos is not None:
            if m == 1:
                new_head = None
                for i in range(n - m + 1):
                    node = pos
                    pos = pos.next



            pos = pos.next
            index += 1


if __name__ == '__main__':
    head = ListNode(1)

    pos = head
    for i in range(2, 11):
        pos.next = ListNode(i)
        pos = pos.next

    s = Solution()
    pos2 = s.reverseBetween(2, 5)

    while pos2 is not None:
        print(pos2.val)
        pos2 = pos2.next
