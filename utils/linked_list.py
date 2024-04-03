"""
@Author: yanzx
@Date: 2021/8/17 23:46
@Description: 
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = None


def create_list(nums: List[int]) -> ListNode:
    if not nums:
        return None
    head = ListNode(nums[0])
    p = head
    for i in range(1, len(nums)):
        p.next = ListNode(nums[i])
        p = p.next
    return head


def print_list(head: ListNode):
    while head is not None:
        print(str(head.val) + "->", end="")
        head = head.next
    print("None")
