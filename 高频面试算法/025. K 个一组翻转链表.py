"""
@Author: yanzx
@Date: 2021-11-24 20:13:06
@Desc: 25. K 个一组翻转链表
输入：head = [1,2,3,  4,5], k = 2
输出：[2,1,4,3,5]

思路：递归翻转
"""

from utils.linked_list import ListNode, create_list, print_list


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 1:
            return head
        tail = head
        # 找到tail
        for i in range(k):
            # 找到tail
            if not tail:
                return head
            tail = tail.next
        new_head = self.reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return new_head

    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        """
        给定头和尾进行反转
        :param head:
        :param tail:
        :return: 返回新的头结点
        """
        new_head = None
        while head is not tail:
            tmp = head
            head = head.next
            tmp.next = new_head
            new_head = tmp
        return new_head


if __name__ == '__main__':
    head = create_list([1, 2, 3, 4, 5, 6, 7, 8])

    s = Solution()

    res = s.reverseKGroup(head, 3)
    print_list(res)
