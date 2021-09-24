"""
@Author: yanzx
@Date: 2021/5/2 23:22
@Description: 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    # 将链表加到数组中
    def sortedListToBST1(self, head: ListNode) -> TreeNode:

        def get_nums(head):
            nums = []
            p = head
            while p:
                nums.append(p.val)
                p = p.next
            return nums
        nums = get_nums(head)

        def helper(left, right):
            if left >= right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left, root.right = helper(left, mid), helper(mid+1, right)
            return root

        return helper(0, len(nums))

    # 链表分治
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 获取链表的中点和中点的前面节点
        def get_mid_node(head: ListNode):
            slow, fast = head, head
            slow_pre = slow
            while fast and fast.next:
                fast = fast.next.next
                slow_pre = slow
                slow = slow.next
            return slow, slow_pre

        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        mid, mid_pre = get_mid_node(head)
        mid_pre.next = None
        root = TreeNode(mid.val)
        root.left, root.right = self.sortedListToBST(head), self.sortedListToBST(mid.next)
        return root

def in_print_tree(root):
    if root is not None:
        # 中序遍历
        in_print_tree(root.left)
        print(root.val)
        in_print_tree(root.right)


def get_head(nums):
    head = ListNode(nums[0])
    p = head
    for i in nums[1:]:
        p.next = ListNode(i)
        p = p.next
    return head



if __name__ == '__main__':
    s = Solution()
    head = get_head(nums=[-10,-3,0,5,9])
    root = s.sortedListToBST(head)
    in_print_tree(root)


