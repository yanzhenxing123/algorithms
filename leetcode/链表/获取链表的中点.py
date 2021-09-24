"""
@Author: yanzx
@Date: 2021/5/2 23:41
@Description: 用 slow作为新的头，即可平等分割两个链表，当链表的节点数为奇数时，则前面的少 后面的多 否则 一样多 [0, 1, | 2, 3, 4]   [0, 1, 2, | 3, 4, 5]
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_mid_node(self, head: ListNode)->ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow



def get_head(nums):
    head = ListNode(nums[0])
    p = head
    for i in nums[1:]:
        p.next = ListNode(i)
        p = p.next
    return head

if __name__ == '__main__':
    nums = [i for i in range(100)]
    head = get_head(nums)
    s = Solution()
    res = s.get_mid_node(head)
    print(res.val)


