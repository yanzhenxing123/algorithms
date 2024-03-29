"""
@Time: 2024/3/28 15:54
@Author: yanzx
@Desc: 
"""
from typing import Optional
from utils.linked_list import print_list, create_list, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        reverse_length = length // 2
        p = head
        pre = None
        for i in range(reverse_length):  # 后边的长度 >= 前边的长度
            pre = p
            p = p.next
        pre.next = None  # 分割

        # 翻转
        new_head = None
        while p:
            q = p.next
            p.next = new_head
            new_head = p
            p = q
        # 判断回文
        while head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True


if __name__ == '__main__':
    head = create_list([1, 2, 2, 1])
    s = Solution()
    res = s.isPalindrome(head)
    print(res)
