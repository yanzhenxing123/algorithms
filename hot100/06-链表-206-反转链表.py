"""
@Time: 2024/3/28 15:14
@Author: yanzx
@Desc: codetop 第3题

"""

from typing import Optional
from utils.linked_list import print_list, create_list, ListNode



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归实现
        1->2->3->None
        pre cur
        :param head:
        :return:
        """
        if not head:
            return head

        def reverse(pre, cur):  # 递归形式的去翻转链表
            """
            两个入参 pre和cur，
            首先记录cur的下一个, 然后翻转当前的
            :param pre:
            :param cur:
            :return:
            """
            if not cur:  # 递归终止的条件，当前为空，返回pre
                return pre
            next = cur.next  # 往后指
            cur.next = pre  # 往前指
            return reverse(cur, next)

        res = reverse(None, head)
        return res

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代实现，先头删，再头插
        :param head:
        :return:
        """
        new_head = None
        p = head
        while p:
            # 先头删
            node = p
            p = p.next
            # 再头插（新链表）
            node.next = new_head
            new_head = node

        return new_head
    
    def reverseList_2nd(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        使用递归的方法
        Args:
            head (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        if not head:
            return
        def reverse(pre, cur):
            if not cur:
                return pre
            next_node = cur.next
            cur.next = pre
            return reverse(cur, next_node)
        
        new_head = reverse(None, head)
        return new_head
        
        
    


if __name__ == '__main__':
    head = create_list([1, 2, 3])
    s = Solution()
    new_head = s.reverseList_2nd(head)
    print_list(new_head)
