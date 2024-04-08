"""
@Time: 2024/4/8 14:52
@Author: yanzx
@Desc:
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        存储random nodes，并且存储旧链表和新链表一一对应的关系
        :param head:
        :return:
        """
        if not head:
            return head
        old_2_new = {}  # 存储一一对应的node
        p = head
        dummy = Node(0)
        q = dummy
        random_nodes = []
        while p:
            if p.random:
                random_nodes.append(hash(p.random))
            else:
                random_nodes.append(None)
            q.next = Node(p.val)
            old_2_new[hash(p)] = q.next
            p = p.next
            q = q.next
        q = dummy.next
        print(random_nodes)
        print(old_2_new)
        for random_node in random_nodes:
            if random_node:
                q.random = old_2_new[random_node]
            else:
                q.random = None
            q = q.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node0.random = None
    node1.random = node3
    node2.random = node2
    node3.random = node1
    s.copyRandomList(node0)
