"""
@Author: yanzx
@Date: 2021-11-24 20:13:06
@Desc: 25. K 个一组翻转链表
输入：head = [1,2,3,  4,5], k = 2
输出：[2,1,4,3,5]

思路：递归翻转
"""

from utils.linked_list import ListNode, create_list, print_list


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1

        # cur每次都到一组的下一个，作为下一个的头节点
        if count != k:
            # 终止条件：一组不够 或者 为 None
            return head

        new_head = self.reverseKGroup(cur, k)

        while count:
            # 反转一组
            count -= 1
            # 头删 tmp = head, head = head.next
            tmp = head
            head = head.next
            # 头插：先tmp.next = new_head, new_head.next = tmp
            tmp.next = new_head
            new_head = tmp

        return new_head



if __name__ == '__main__':
    head = create_list([1, 2, 3, 4, 5, 6, 7, 8])

    s = Solution()
    res = s.reverseKGroup(head, 3)
    print_list(res)
