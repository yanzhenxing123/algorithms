"""
@Author: yanzx
@Date: 2021/8/4 22:56
@Description: 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
新的一个头 指向 小的那一个
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        if not l1 and not l2:
            return l1
        if l1.val < l2.val:
            root = l1
            l1 = l1.next
        else:
            root = l2
            l2 = l2.next
        p = root
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return root





if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    s = Solution()
    root = s.mergeTwoLists(l1, l2)
    while root:
        print(root.val)
        root = root.next
