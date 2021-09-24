"""
@Author: yanzx
@Date: 2020/8/4 15:09
@Description: 删除链表的倒数第N个节点
1.递归解决（妙啊）
2.普通的方法解决
"""

# class Solution:
#     curr = 0
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if not head:
#             return None
#         head.next = self.removeNthFromEnd(head.next, n)
#         Solution.curr += 1
#         if n == Solution.curr:
#             return head.next
#         return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    count = 0
    pos = head
    while pos != None:
        count += 1
        pos = pos.next
    index = count - n + 1
    if index == 1:
        head = head.next

    if index > 1:
        pos = head
        for _ in range(index - 2):
            pos = pos.next
        pos.next = pos.next.next
    return head


if __name__ == '__main__':
    head = ListNode(1)
    pos = head
    for i in range(2, 11):
        pos.next = ListNode(i)
        pos = pos.next

    new_head = removeNthFromEnd(head, 9)

    pos = new_head
    while pos is not None:
        print(pos.val)
        pos = pos.next
