"""
@Time: 2024/4/6 22:06
@Author: yanzx
@Desc:

l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""

from typing import Optional
from utils.linked_list import ListNode, create_list, print_list
import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        循环终止条件l1 or l2
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        new_head = ListNode(0)
        p = new_head
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            value = l1_val + l2_val + carry
            carry = value // 10
            p.next = ListNode(value % 10)
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            p.next = ListNode(carry)
        return new_head.next


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 9]

    l2 = [5, 6, 4, 9]

    l1 = create_list(l1)
    l2 = create_list(l2)
    res = s.addTwoNumbers(l1, l2)
    print_list(res)
