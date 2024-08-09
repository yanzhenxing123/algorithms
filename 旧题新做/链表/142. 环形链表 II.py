"""
@Time:
@Author: yanzx
@Desc: 
"""

from utils.linked_list import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not ListNode:
            return None

        slow = fast = head

        flag = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break

        if not flag:
            return None

        p = head

        while p != slow:
            p = p.next
            slow = slow.next
        return p
