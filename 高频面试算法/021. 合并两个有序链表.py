"""
@Author: yanzx
@Date: 2022/4/4 23:06
@Description: 21. 合并两个有序链表

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from utils.linked_list import ListNode, print_list, create_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 新头，两个链表同时遍历
        if not list1:
            return list2
        if not list2:
            return list1

        pos1, pos2 = list1, list2
        if pos1.val <= pos2.val:
            head = pos1
            pos1 = pos1.next
        else:
            head = pos2
            pos2 = pos2.next
        pos = head


        while pos1 is not None and pos2 is not None:
            if pos1.val <= pos2.val:
                pos.next = pos1
                pos1 = pos1.next
            else:
                pos.next = pos2
                pos2 = pos2.next
            pos = pos.next
        if pos1:
            pos.next = pos1
        else:
            pos.next = pos2

        return head


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    s = Solution()
    head1 = create_list(l1)
    head2 = create_list(l2)
    print_list(head1)
    print_list(head2)
    res = s.mergeTwoLists(head1, head2)
    print_list(res)
