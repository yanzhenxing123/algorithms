"""
@Author: yanzx
@Date: 2021-11-24 15:21:25
@Desc: 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
head
1 -> 2 -> 3 -> 4 -> 5

"""

from utils.linked_list import create_list, ListNode, print_list


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 原链表头删 新链表头插入
        new_head = None
        while head:
            tmp = head
            head = head.next
            tmp.next = new_head
            new_head = tmp
        return new_head


if __name__ == '__main__':
    s = Solution()
    head = create_list([i for i in range(5)])
    res = s.reverseList(head)
    print_list(res)
