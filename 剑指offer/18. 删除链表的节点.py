"""
@Author: yanzx
@Date: 2021/8/18 22:41
@Description: 
"""
from basis.utils.linked_list import ListNode, create_list, print_list

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        p = head
        pre = p
        while p.val != val:
            pre = p
            p = p.next
        pre.next = p.next

        return head


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 1, 9]
    val = 5
    head = create_list(nums)
    res = s.deleteNode(head, val)
    print_list(res)