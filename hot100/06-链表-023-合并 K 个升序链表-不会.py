"""
@Time: 2024/4/13 14:59
@Author: yanzx
@Desc:
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""
from typing import Optional, List
from utils.linked_list import print_list, create_list, ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        相当于归并排序的合并过程
        :param lists:
        :return:
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        length = len(lists)
        left, right = 0, length - 1
        mid = (left + right) // 2
        head1 = self.mergeKLists(lists[left:mid + 1])
        head2 = self.mergeKLists(lists[mid + 1:right + 1])
        return self.merge(head1, head2)

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
        return new_head.next

    def mergeKLists_2nd(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            dummy = ListNode(-1)
            p = dummy
            while left and right:
                if left.val <= right.val:
                    p.next = left
                    left = left.next
                else:
                    p.next = right
                    right = right.next
                p = p.next

            p.next = left if left else right
            return dummy.next

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        length = len(lists)
        left, right = 0, length - 1
        mid = (left + right) // 2
        head1 = self.mergeKLists(lists[left:mid + 1])
        head2 = self.mergeKLists(lists[mid + 1:right + 1])
        return self.merge(head1, head2)



if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3, 4, 5, 7]
    nums2 = [2, 5, 6, 7, 8]
    head1 = create_list(nums1)
    head2 = create_list(nums2)
    lists = [head1, head2]
    res = s.mergeKLists(lists)
    print_list(res)
