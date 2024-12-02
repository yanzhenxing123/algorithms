"""
@Time: 2024/8/9 13:49
@Author: yanzx
@Desc: 
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        1. 判断是否有环（队尾是否是同一个），并记录长度 length_a, length_b
        2. 如何找环？假设B长，则让先走B length_b - length_a个，然后一起走得到第一个一样的就是
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None

        p1, p2 = headA, headB
        length_a = 0
        length_b = 0
        while p1:
            length_a += 1
            p1 = p1.next

        while p2:
            length_b += 1
            p2 = p2.next
        if p1 != p2:  # 无环
            return None
        p1, p2 = headA, headB
        delta = abs(length_a - length_b)
        if length_a > length_b:
            for i in range(delta):
                p1 = p1.next
        else:
            for i in range(delta):
                p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1