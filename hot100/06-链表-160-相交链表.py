"""
@Time: 2024/3/28 10:36
@Author: yanzx
@Desc:
"""
from utils.linked_list import ListNode
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        1. 并记录长度 length_a, length_b
        2. 假设B长，则让先走B length_b - length_a个，然后一起走判断是否相交
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        pre_p1 = None
        pre_p2 = None
        length_a = 0
        length_b = 0
        while p1:
            length_a += 1
            pre_p1 = p1
            p1 = p1.next

        while p2:
            length_b += 1
            pre_p2 = p2
            p2 = p2.next
        if pre_p1 != pre_p2:  # 无环
            return None
        p1, p2 = headA, headB
        delta = abs(length_a - length_b)
        if length_a > length_b:
            for i in range(delta):
                p1 = p1.next
        else:
            for i in range(delta):
                p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        将B的tail指向head形成环，从A出发看能不能找到那个环
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB

        while p1.next:
            p1 = p1.next
        tail = p1
        tail.next = headA

        # 1. 对headB检测是否有环
        slow, fast = headB, headB
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                flag = True
                break
        if not flag:
            return None
        pos = headB
        while pos != slow:
            pos = pos.next
            slow = slow.next
        tail.next = None
        return pos

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        暴力O(n^2)c超时
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        p1 = headA
        while p1:
            p2 = headB
            while p2:
                if p2 == p1:
                    return p2
                p2 = p2.next
            p1 = p1.next
        return None