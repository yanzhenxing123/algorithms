"""
@Time: 2024/4/7 10:35
@Author: yanzx
@Desc:
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

dummy -> 1 -> 2 -> 3 -> 4 -> 5
   p
"""
from typing import Optional
from utils.linked_list import ListNode, create_list, print_list
import random


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        反转k个链表的时候需要知道头和尾巴，每一次p在前一组的最后一个
        :param head:
        :param k:
        :return:
        """
        if not head or not head.next or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while True:
            pos = p
            count = k
            while pos.next and count:  # 判断是否反转
                pos = pos.next
                count -= 1
            if count == 0:  # 说明这一组为可翻转的
                next_group_head = pos.next
                new_head, tail = self.reverse_k(p.next, k)  # 反转这一组
                p.next = new_head
                p = tail
                p.next = next_group_head
            else:  # 不可翻转则直接返回
                return dummy.next

    def reverse_k(self, head: Optional[ListNode], k):
        """
        返回新的头和尾巴
        :param head:
        :return:
        """
        p = head
        tail = head
        new_head = None
        for i in range(k):
            node = p
            p = p.next
            node.next = new_head
            new_head = node
        return new_head, tail


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    k = 2
    head = create_list(head)
    s = Solution()
    res = s.reverseKGroup(head, k)
    print_list(res)
