"""
@Author: yanzx
@Date: 2020/7/30 10:16
@Description:
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 计算长度
        length = 0
        pos = head
        while pos != None:
            length += 1
            pos = pos.next

        # 判断
        if head.next == None or k <= 1 or k > length:
            return head

        prv = head
        end = self.find_end(head, k)
        new_new_head = self.reverse(head, k)
        for i in range(length // k):
            if end is not None:
                temp = self.find_end(end, k)
                if i != length // k - 1:
                    new_head = self.reverse(end, k)

                # 最后一组
                else:
                    new_head = end
                prv.next = new_head
                prv = end
                end = temp
            else:
                break
        return new_new_head

    # 找到一段的一个
    def find_end(self, head, k):
        for _ in range(k):
            if head is not None:
                head = head.next
            else:
                break
        return head

    # 反转链表
    def reverse(self, head, k):
        new_head = None
        pos = head
        for _ in range(k):
            if head != None:
                node = head
                head = head.next
                node.next = new_head
                new_head = node
            else:
                return pos
        return new_head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    pos = head
    for i in range(2, 4):
        pos.next = ListNode(i)
        pos = pos.next

    new_head = s.reverseKGroup(head, k=3)
    pos = new_head
    while pos != None:
        print(pos.val)
        pos = pos.next
