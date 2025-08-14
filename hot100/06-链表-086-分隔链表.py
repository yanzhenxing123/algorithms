"""
@Author: yanzx
@Date: 2025/3/10 11:09
@Description:
"""
from typing import Optional

from utils.linked_list import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # write your code here.
        left_head = ListNode(0)
        right_head = ListNode(0)
        left = left_head
        right = right_head
        p = head
        while p:
            if p.val < x:
                left.next = p
                left = left.next
            else:
                right.next = p
                right = right.next
            p = p.next
        left.next = right_head.next
        right_head.next = None
        right.next = None
        return left_head.next


        