"""
@Author: yanzx
@Date: 2021/4/6 23:53
@Description: 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head




if __name__ == '__main__':
    s = Solution()

