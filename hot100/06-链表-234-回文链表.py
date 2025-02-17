"""
@Time: 2024/3/28 15:54
@Author: yanzx
@Desc:
给你一个单链表的头节点 head ，请你判断该链表是否为
回文链表
。如果是，返回 true ；否则，返回 false 。



示例 1：

输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false
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
        """
        先找到中点，然后切开，然后将后边的翻转
        判断这两个是不是一样的即可
        且 len(new_head) >= len(head), 故while 判断时使用head
        :param head:
        :return:
        """
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
            node = p
            p = p.next
            node.next = new_head
            new_head = node
        print_list(head)
        print_list(new_head)
        # 判断回文
        while head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True


if __name__ == '__main__':
    head = create_list([1, 2, 1, 2, 1])
    s = Solution()
    res = s.isPalindrome(head)
    print(res)
