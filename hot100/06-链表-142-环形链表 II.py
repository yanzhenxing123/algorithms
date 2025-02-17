"""
@Time: 2024/4/6 11:48
@Author: yanzx
@Desc: 
"""

from utils.linked_list import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast = slow = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return None
        pos = head
        while pos != slow:
            pos = pos.next
            slow = slow.next
        return pos
