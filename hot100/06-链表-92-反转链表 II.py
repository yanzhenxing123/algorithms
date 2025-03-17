"""
@Author: yanzx
@Date: 2025/3/17 16:32
@Description:
汇量科技一面
快手一面
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]
"""

from typing import Optional

from utils.linked_list import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        1. 先分割
        2. 再翻转
        3. 再合并
        需要知道三个节点

        left_tail
        mid_head
        mid_tail

        :param head:
        :param left:
        :param right:
        :return:
        """
        if not head or not head.next or left == right:
            return head
        p = head
        count = 0
        while p:
            count += 1
            if count == left:
                left = p
            elif count == right:
                right = p
            p = p.next

        dummy = ListNode(0)
        dummy.next = head

        # left左边节点
        left_head = dummy
        mid_head = left
        mid_tail = right
        p = dummy
        while p and p.next != left:
            p = p.next
        left_tail = p
        left_tail.next = None

        right_head = right.next
        mid_tail.next = None

        # 翻转
        p = mid_head
        new_head = None
        while p:
            node = p
            p = p.next
            node.next = new_head
            new_head = node

        left_tail.next = new_head
        left.next = right_head

        return dummy.next
