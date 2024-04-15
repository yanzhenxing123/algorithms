"""
@Time: 2024/3/28 15:14
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归实现
        1->2->3->None
        pre cur
        :param head:
        :return:
        """
        if not head:
            return head

        def reverse(pre, cur):
            if not cur:
                return pre
            q = cur.next
            cur.next = pre
            return reverse(cur, q)

        res = reverse(None, head)
        return res

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代实现，先头删，再头插
        :param head:
        :return:
        """
        new_head = None
        p = head
        while p:
            q = p.next
            p.next = new_head
            new_head = p
            p = q

        return new_head


if __name__ == '__main__':
    head = create_list([1, 2, 3])
    s = Solution()
    new_head = s.reverseList(head)
    print_list(new_head)
