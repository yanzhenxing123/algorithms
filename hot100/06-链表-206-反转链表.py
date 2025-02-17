"""
@Time: 2024/3/28 15:14
@Author: yanzx
@Desc: 
"""

from typing import Optional
from utils.linked_list import print_list, create_list, ListNode


## Definition for singly-linked list.
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
            """
            :param pre: 前一个
            :param cur: 当前
            :return:
            """
            if not cur:
                return pre
            q = cur.next  # 往后指
            cur.next = pre  # 往前指
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
            # 先头删
            node = p
            p = p.next
            # 再头插（新链表）
            node.next = new_head
            new_head = node

        return new_head


if __name__ == '__main__':
    head = create_list([1, 2, 3])
    s = Solution()
    new_head = s.reverseList(head)
    print_list(new_head)
