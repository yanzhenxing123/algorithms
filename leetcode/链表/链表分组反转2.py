"""
@Author: yanzx
@Date: 2020/7/30 11:31
@Description: 
"""

# Definition for singly-linked list.
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

        # 计算链表长度
        length = 0
        pos = head
        while pos != None:
            length += 1
            pos = pos.next

        # 判断
        if k <= 1 or k > length:
            return head

        # 核心代码
        # 先进行反转一次
        prv = head  # pre负责连接
        end = self.find_end(head, k)
        new_new_head = self.reverse(head, k)
        times = length // k
        for i in range(times):
            # 如果是整数倍则最后一次不进行操作
            if end is not None:
                temp = self.find_end(end, k)
                # 判断是不是最后一组，最后一组不进行反转
                if i != times - 1:
                    new_head = self.reverse(end, k)
                else:
                    new_head = end
                prv.next = new_head
                prv = end
                end = temp
            else:
                break
        return new_new_head

    # 找到下一段的第一个
    def find_end(self, head, k):
        for _ in range(k):
            if head is not None:
                head = head.next
            # 最后一组 不用管
            else:
                break
        return head

    # 反转链表
    def reverse(self, head, k):
        new_head = None
        for _ in range(k):
            # 头删
            node = head
            head = head.next

            # 头插
            node.next = new_head
            new_head = node
        return new_head


# 测试代码
if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    pos = head
    for i in range(2, 6):
        pos.next = ListNode(i)
        pos = pos.next

    new_head = s.reverseKGroup(head, k=3)
    pos = new_head
    while pos != None:
        print(pos.val)
        pos = pos.next