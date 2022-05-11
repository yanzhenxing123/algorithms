"""
@Author: yanzx
@Date: 2022/4/5 23:20
@Description: 
"""

from typing import Optional
from utils.linked_list import ListNode, create_list, print_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head
        # 快指针，如果有环，那么一定是二者的交点
        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
