"""
@Author: yanzx
@Date: 2020/12/18 14:46
@Description: 环形链表2
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        fast = slow = head
        fast = slow.next
        flag = False
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                flag = True
                break

        if not flag:
            return None
        pos = head
        while pos is not slow:
            pos = pos.next
            slow = slow.next

        return pos


if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    a = ListNode(2)
    head.next = a
    b = ListNode(0)
    c = ListNode(-4)
    a.next = b
    b.next = c
    c.next = a
    res = s.detectCycle(head=head)
    print(res)

