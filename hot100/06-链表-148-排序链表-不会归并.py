"""
@Time: 2024/3/27 23:24
@Author: yanzx
@Desc: 
"""

from typing import Optional
from utils.linked_list import ListNode, create_list, print_list
import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        先分再合
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        # 1. 分开，左边长度一定大于等于右边长度
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        # 2. 合并
        new_head = self.merge(left, right)
        return new_head

    def merge(self, left, right):
        p = new_head = ListNode(-1)
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        print_list(new_head)
        return new_head.next

    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        暴力求解 每次选最大的进行头插，可以得到的时间复杂度为O(n^2)的排序算法，所以不行
        不行
        :param head:
        :return:
        """
        new_head = None
        if not head:
            return None

        while head:
            p = head
            pre = None
            max_node = p
            while p:
                if p.val > max_node.val:
                    max_node = p
                    max_node_pre = pre

                pre = p
                p = p.next
            if max_node == head:
                head = max_node.next
            else:
                # 删除
                max_node_pre.next = max_node.next
            # 头插
            max_node.next = new_head
            new_head = max_node


        return new_head


if __name__ == '__main__':
    s = Solution()
    nums = [random.randint(1, 100) for i in range(5)]
    head = create_list(nums)
    print_list(head)
    head = s.sortList(head)
    print_list(head)
