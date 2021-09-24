'''
      给出两个 非空 的链表用来表示两个非负的整数。
      其中，它们各自的位数是按照 逆序 的方式存储的，
      并且它们的每个节点只能存储 一位 数字。
      如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
      您可以假设除了数字 0 之外，这两个数都不会以 0 开头
      输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
      输出：7 -> 0 -> 8
      原因：342 + 465 = 807
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    n = l1.val + l2.val
    l3 = ListNode(n % 10)
    l3.next = ListNode(n // 10)
    # 注意这个地方
    p1 = l1.next
    p2 = l2.next
    p3 = l3
    while True:
        if p1 and p2:
            n = p1.val + p2.val + p3.next.val
            p3.next.val = n % 10
            p3.next.next = ListNode(n // 10)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        elif p1 is None and p2 is not None:
            n = p2.val + p3.next.val
            p3.next.val = n % 10
            p3.next.next = ListNode(n // 10)
            p2 = p2.next
            p3 = p3.next
        elif p1 is not None and p2 is None:
            n = p1.val + p3.next.val
            p3.next.val = n % 10
            p3.next.next = ListNode(n // 10)
            p1 = p1.next
            p3 = p3.next
        else:
            if p3.next.val == 0:
                p3.next = None
            break
    return l3
