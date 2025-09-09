"""
@Author: yanzx
@Time: 2025/9/8 23:11 
@Description: 
"""

from utils.linked_list import ListNode, create_list, print_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return

        # (1) Find the middle of the linked list
        def findMidNode(head: ListNode) -> ListNode:
            slow, fast = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        # (2) Reverse the second part of the linked list
        def reverseNodeList(head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            newHead = reverseNodeList(head.next)
            head.next.next = head
            head.next = None
            return newHead

        # (3) Merge the two parts of the linked list
        def mergeNodeList(firstList: ListNode, secondList: ListNode) -> None:
            while firstList and secondList:
                temp1 = firstList.next
                temp2 = secondList.next
                firstList.next = secondList
                secondList.next = temp1
                firstList = temp1
                secondList = temp2

        dummy = ListNode(0)
        dummy.next = head
        mid = findMidNode(dummy)
        secondList = reverseNodeList(mid.next)
        mid.next = None  # Split the list into two parts
        mergeNodeList(head, secondList)


if __name__ == '__main__':
    head = [1, 2, 3, 4]
    head = create_list(head)
    print_list(head)

    s = Solution()
    s.reorderList(head)
