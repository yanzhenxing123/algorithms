"""
@Author: yanzx
@Date: 2022/5/11 22:48
@Description: 
"""
import gc

from utils.linked_list import ListNode, create_list, print_list

def del_x(head: ListNode, x: int) -> ListNode:
    if not head:
        return None
    if head.val == x:
        return del_x(head.next, x)
    head.next = del_x(head.next, x)
    return head

if __name__ == '__main__':
    head = create_list([2] + [i for i in range(10)] + [2, 3, 10] + [10])
    print_list(head)
    res = del_x(head, 2)
    print_list(res)

