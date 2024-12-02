"""
@Time: 2024/8/9 15:23
@Author: yanzx
@Desc: 
"""
from typing import Optional

from utils.linked_list import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def func(pre, current):
            if not current:
                return pre
            p = current.next
            current.next = pre
            return func(current, p)

        return func(None, head)

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = None
        p = head
        while p:
            node = p
            p = p.next
            node.next = new_head
            new_head = node
        return new_head


if __name__ == '__main__':
    s = Solution()
