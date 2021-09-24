"""
@Author: yanzx
@Date: 2020/12/19 21:11
@Description: 
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pos = head
        pos_big = pos_small = new_head_big = new_head_small = None
        while pos is not None:
            if pos.val < x:
                if new_head_small is not None:
                    pos_small.next = pos
                    pos_small = pos
                else:
                    new_head_small = pos
                    pos_small = pos
            else:
                if new_head_big is not None:
                    pos_big.next = pos
                    pos_big = pos
                else:
                    new_head_big = pos
                    pos_big = pos
            pos = pos.next

        if not new_head_small:
            return new_head_big

        pos_small.next = new_head_big
        if pos_big:
            pos_big.next = None
        return new_head_small

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    res = s.partition(head, 3)
    while res is not None:
        print(res.val)
        res = res.next





