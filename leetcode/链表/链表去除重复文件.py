"""
@Author: yanzx
@Date: 2020/7/31 14:49
@Description: 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(head):
    flag = False
    if head != None and head.next != None:
        new_head = pos = head
        next = pos.next
        times = 0
        while next != None:
            times += 1
            prv = pos
            pos = pos.next
            next = pos.next
            if next != None:
                if times == 1:
                    if prv.val == pos.val:
                        flag = True
                if prv.val != pos.val and pos.val != next.val:
                    new_head.next = pos
                    new_head = pos
            else:
                if times == 1:
                    if prv.val == pos.val:
                        flag = True
                if prv.val != pos.val:
                    new_head.next = pos
                else:
                    new_head.next = None
        if flag:
            head = head.next

        return head
    else:
        return head



if __name__ == '__main__':
    pos = head = ListNode(1)
    pos.next = ListNode(1)
    pos = pos.next

    head = solution(head)

    while head != None:
        print(head.val)
        head = head.next
