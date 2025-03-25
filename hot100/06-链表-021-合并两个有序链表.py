"""
@Time: 2024/3/30 08:09
@Author: yanzx
@Desc:
"""

from typing import Optional
from utils.linked_list import print_list, create_list, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        new_head = ListNode()
        p = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        p.next = list1 if not list2 else list2
        return new_head.next

    def mergeTwoLists_2nd(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dumpy = ListNode(0)
        p_1 = list1
        p_2 = list2
        q = dumpy
        while p_1 and p_2:
            if p_1.val >= p_2.val:
                q.next = p_1
                p_1 = p_1.next
            else:
                q.next = p_2
                p_2 = p_2.next
            q = q.next

        if not p_1:
            q.next = p_2
        if not p_2:
            q.next = p_1
        return dumpy.next




if __name__ == '__main__':
    s = Solution()
    head1 = create_list([1, 2, 5, 6])
    head2 = create_list([2, 3, 6, 7])
    res = s.mergeTwoLists(head1, head2)
    print_list(res)
