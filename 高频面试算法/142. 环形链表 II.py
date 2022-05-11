"""
@Author: yanzx
@Date: 2021-12-01 20:29:58
@Desc:

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

"""
from utils.linked_list import ListNode, create_list, print_list


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        快慢指针，快指针走2步，慢指针后走1步, 二者相遇，让慢指针重返前线，快指针不再快，也是走一步
        :param head:
        :return:
        """
        if not head:
            return None
        flag = False
        fast, slow = head, head
        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                flag = True
                break

        if not flag:
            return None

        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return fast



    def detectCycle1(self, head: ListNode) -> ListNode:
        if not head:
            return head
        fast = slow = head

        while True:
            fast = fast.next
            if fast is None:
                return fast
            fast = fast.next
            if fast is None:
                return fast
            slow = slow.next
            if slow is fast:
                break

        slow = head
        while slow is not fast:
            fast = fast.next
            slow = slow.next
            if fast is slow:
                break
        return slow




if __name__ == '__main__':
    s = Solution()
    head = create_list([1, 2, 3, 4])
    pos = head
    pos = pos.next.next.next
    pos.next = head
    res = s.detectCycle(pos)
    print(res)
