"""
@Author: yanzx
@Date: 2020/11/6 20:03
@Description:
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hash_set = set()
        pos = head
        while pos is not None:
            hash_code = id(pos)
            if hash_code in hash_set:
                return True
            hash_set.add(hash_code)
            pos = pos.next

        return False

    def hasCycle_2nd(self, head: ListNode) -> bool:
        if not head:
            return False

        fast = slow = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    # 创建一个环形链表
    head = ListNode(1)

    pos = head
    for i in range(2, 11):
        pos.next = ListNode(10)
        print(hash(pos))
        pos = pos.next

    res = s.hasCycle(head)
