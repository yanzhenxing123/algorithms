"""
@Time: 2024/4/7 09:57
@Author: yanzx
@Desc: 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
输入：head = [1,2,3,4]
输出：[2,1,4,3]

"""
from typing import Optional
from utils.linked_list import ListNode, create_list, print_list
import random


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        先切分存到列表中，然后遍历
        :param head:
        :return:
        """
        if not head:
            return None
        p = head
        li = []
        while p: # 两个放一组
            li.append(p)
            p = p.next
            if p:
                node = p
                p = p.next
                node.next = None
        new_li = []
        for tmp_head in li:
            # 反转
            if tmp_head and tmp_head.next:
                new_head = tmp_head.next
                new_head.next = tmp_head
                tmp_head.next = None
            else:
                new_head = tmp_head
            new_li.append(new_head)

        for i in range(len(new_li) - 1):  # 合并
            tmp_head = new_li[i]
            tmp_head.next.next = new_li[i + 1]
        return new_li[0]

    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head
    #     head1 = head
    #     head2 = head.next
    #     p1 = head1
    #     p2 = head2
    #     while p2:  # 分开
    #         p1.next = p2.next
    #         if p2.next:
    #             p2.next = p2.next.next
    #         p1 = p1.next
    #         p2 = p2.next
    #     p1 = head1
    #     p2 = head2
    #     new_head = ListNode(0)
    #     p = new_head
    #     while p1 and p2:  # 合并
    #         p1_next = p1.next
    #         p2_next = p2.next
    #         p.next = p2
    #         p.next.next = p1
    #         p1 = p1_next
    #         p2 = p2_next
    #         p = p.next.next
    #     if p1:
    #         p.next = p1
    #     if p2:
    #         p.next = p2
    #     return new_head.next

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归实现 最优解
        1->2->3->4->5->6->7->8
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head
        new_head = head.next
        head.next = self.swapPairs2(new_head.next)
        new_head.next = head
        return new_head


if __name__ == '__main__':
    nums = [1, 2]
    head = create_list(nums)
    s = Solution()
    res = s.swapPairs(head)
    print_list(res)
