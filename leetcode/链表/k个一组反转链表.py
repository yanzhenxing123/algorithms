"""
@Author: yanzx
@Date: 2021-11-24 09:58:53
@Desc:
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)  # 头结点
        p = dummy
        while True:
            count = k
            stack = []
            new_head = head
            while count and new_head:
                stack.append(new_head)
                new_head = new_head.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下链表连接起来
            p.next = new_head
            head = new_head

        return dummy.next
