"""
@Author: yanzx
@Date: 2021/8/18 22:48
@Description: hash表进行建立
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        p = head
        hashmap = {}
        while p:
            hashmap[p] = Node(p.val)
            p = p.next

        p = head

        while p:
            hashmap[p].next = p.next
            hashmap[p].random = p.random
            p = p.next

        return hashmap[head]

if __name__ == '__main__':
    s = Solution()
