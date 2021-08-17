"""
@Author: yanzx
@Date: 2021/8/17 23:45
@Description:

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

"""

from basis.utils.linked_list import ListNode, create_list, print_list


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        slow = head
        fast = head
        for i in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow



if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    head = create_list(nums)
    res = s.getKthFromEnd(head, 3)
    print_list(res)

