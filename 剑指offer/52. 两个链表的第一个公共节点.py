"""
@Author: yanzx
@Date: 2021-10-04 16:29:51
@Desc: 52. 两个链表的第一个公共节点

"""
from utils.linked_list import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        length_A, length_B = 0, 0
        while pA is not None:
            pA = pA.next
            length_A += 1
        while pB is not None:
            pB = pB.next
            length_B += 1

        if length_A >= length_B:
            p1, p2 = headA, headB
            delta = length_A - length_B
        else:
            p1, p2 = headB, headA
            delta = length_B - length_A
        for i in range(delta):
            p1 = p1.next

        while True:
            if p1 is p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1




if __name__ == '__main__':
    pass
