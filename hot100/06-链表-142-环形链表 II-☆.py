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


    def detectCycle_2nd(self, head: ListNode) -> ListNode:
        """ 
        判断完后，让slow走一个，另一个回到head，每次走一个，最终会在节点遇到
        Args:
            head (ListNode): _description_

        Returns:
            ListNode: _description_
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        flag = False # 有环
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return None
        p = dummy
        while p != slow:
            p = p.next
            slow = slow.next
        return p
        
