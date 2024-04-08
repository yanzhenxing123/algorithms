"""
@Time: 2024/4/6 23:02
@Author: yanzx
@Desc: 
"""

from typing import Optional
from utils.linked_list import ListNode, create_list, print_list
import random


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        p1先走n+1个，p2就是要删除节点的前一个
        :param head:
        :param n:
        :return:
        """
        p1 = p2 = head
        for i in range(n + 1):
            if not p1:  # 如果是倒数第n个，也就是第一个
                return head.next
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 9, 10]
    l1 = create_list(l1)
    res = s.removeNthFromEnd(l1, 4)
    print_list(res)
