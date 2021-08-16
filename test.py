"""
@Author: yanzx
@Date: 2021-07-30 11:38:13
@Desc:
"""
import unittest


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Test(unittest.TestCase):
    def testMergeLinklist(self, l1: ListNode, l2: ListNode):
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2

        if not l1 and not l2:
            return l1

        if l1.val > l2.val:
            root = l2
            l2 = l2.next

        else:
            root = l1
            l1 = l1.next

        p = root

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next

        if l1:
            p.next = l1
        if l2:
            p.next = l2

        return rooooo
