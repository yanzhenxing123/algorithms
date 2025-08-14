"""
@Time: 2024/4/7 10:35
@Author: yanzx
@Desc:
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

dummy -> 1 -> 2 -> 3 -> 4 -> 5


最后一组如果不满足就不用翻转


链表-025-K 个一组翻转链表-☆.py

链表-024-两两交换链表中的节点.py
   
"""
from typing import Optional
from utils.linked_list import ListNode, create_list, print_list
import random


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        题24是两个一组反转链表
        1. 先分组
        2. 反转
        3. 链接
        :param head:
        :param k:
        :return:
        """
        if not head or k == 1:
            return head
        p = head
        li = []
        end_head = None  # 存储最后不翻转的
        while p:
            count = 0
            tmp_head = p
            for i in range(k):
                if p:
                    count += 1
                    pre = p
                    p = p.next
            # 如果长度为k
            if count == k:
                print(count)
                li.append(tmp_head)
                pre.next = None
            else:
                end_head = tmp_head
        new_li = []
        for tmp_head in li:
            new_head = self.reverse_list(tmp_head)
            new_li.append(new_head)
        for i in range(len(new_li)):
            p = new_li[i]
            while p.next:
                p = p.next
            if i == len(new_li) - 1:
                p.next = end_head
            else:
                p.next = new_li[i + 1]
        return new_li[0]

    def reverseKGroup_3rd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        和24题一样，分组进行,最优版本
        Args:
            head (Optional[ListNode]): _description_
            k (int): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        if not head or not head.next or k  == 1:
            return head
        # 1. 分组
        p = head
        node_li = []
        while p:
            tmp_head = p
            count = 0
            for i in range(k):
                if p:
                    pre = p
                    p = p.next
                    count+=1 
            if count == k:
                pre.next = None
                # 翻转
                new_tmp_head = self.reverse_list(tmp_head)
            else:
                new_tmp_head = tmp_head
            node_li.append(new_tmp_head)   
        
        for i in range(len(node_li) - 1):
            p = node_li[0]
            while p.next:
                p = p.next
            p.next = node_li[i+1]
        return node_li[0]
            
    def main():
        """_summary_
        """
        

    def reverse_list(self, head):
        if not head:
            return None
        new_head = None
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        return new_head

    def reverseKGroup_2nd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 先将链表进行分割，然后进行翻转
        if not head or not head.next or k == 1:
            return head
        p = head
        head_li = []
        end_head = None
        while p:
            tmp_head = p
            pre = None
            count = 0
            for i in range(k):
                if p:
                    pre = p
                    p = p.next
                    count += 1
            if count == k:  # 说明这一组要翻转
                head_li.append(tmp_head)
                pre.next = None
            else:  # 最后一组特殊处理
                end_head = tmp_head

        # 最head_li中的head进行翻转
        new_head_li = []
        for tmp_head in head_li:
            new_head = self.reverse_list(tmp_head)
            new_head_li.append(new_head)
        for i in range(len(new_head_li)):
            new_head = new_head_li[i]
            p = new_head
            while p.next:
                p = p.next
            if i == len(new_head_li) - 1:  # 对最后一个特殊处理
                p.next = end_head
            else:
                p.next = new_head_li[i + 1]
        return new_head_li[0]

    def reverseKGroup1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        反转k个链表的时候需要知道头和尾巴，每一次p在前一组的最后一个
        :param head:
        :param k:
        :return:
        """
        if not head or not head.next or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while True:
            pos = p
            count = k
            while pos.next and count:  # 判断是否反转
                pos = pos.next
                count -= 1
            if count == 0:  # 说明这一组为可翻转的
                next_group_head = pos.next
                new_head, tail = self.reverse_k(p.next, k)  # 反转这一组
                p.next = new_head
                p = tail
                p.next = next_group_head
            else:  # 不可翻转则直接返回
                return dummy.next

    def reverse_k(self, head: Optional[ListNode], k):
        """
        返回新的头和尾巴
        :param head:
        :return:
        """
        p = head
        tail = head
        new_head = None
        for i in range(k):
            node = p
            p = p.next
            node.next = new_head
            new_head = node
        return new_head, tail


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    k = 3
    head = create_list(head)
    s = Solution()
    res = s.reverseKGroup(head, k)
    print_list(res)
