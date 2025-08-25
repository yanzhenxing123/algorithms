"""
@Time:
@Author: yanzx
@Desc:
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。



示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]



"""
from typing import Optional
from utils.linked_list import print_list, create_list, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        length = 0

        p = head
        while p:
            p = p.next
            length += 1


        k = k % length
        if k == 0:
            return head

        steps = length - k - 1
        q = head
        for i in range(steps):
            q = q.next

        new_head = q.next
        print(new_head.val)
        q.next = None
        p = new_head

        while p.next:
            p = p.next

        p.next = head

        return new_head




if __name__ == '__main__':
    head = create_list([1, 2, 3, 4, 5])
    s = Solution()
    res = s.rotateRight(head, 2)
    print_list(res)
