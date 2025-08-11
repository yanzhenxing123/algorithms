"""
@Time: 2024/4/6 11:05
@Author: yanzx
@Desc:

"""

from typing import Optional
from utils.linked_list import ListNode, create_list, print_list
import random


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        快慢指针
        :param head:
        :return:
        """
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
    def hasCycle_2nd(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        


if __name__ == '__main__':
    head = [3, 2, 0, -4]
    create_list(head)
    s = Solution()
