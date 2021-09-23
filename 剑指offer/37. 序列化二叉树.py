"""
@Author: yanzx
@Date: 2021-09-22 23:36:25
@Desc:
请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

按照层序遍历进行encode和decode

"""

from utils.binary_tree import TreeNode, create_tree, floor_print
from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        res = ""
        while queue:
            root = queue.pop(0)
            if root is not None:
                queue.append(root.left)
                queue.append(root.right)
                res = res + " " + str(root.val)
            else:
                res = res + " " + "None"
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split()
        root = TreeNode(int(arr[0]))
        index = 1
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if arr[index] != 'None':
                left_node = TreeNode(int(arr[index]))
                node.left = left_node
                queue.append(left_node)
            index += 1
            if arr[index] != 'None':
                right_node = TreeNode(int(arr[index]))
                node.right = right_node
                queue.append(right_node)
            index += 1
        return root


if __name__ == '__main__':
    codec = Codec()
    root = create_tree([1, 2, 3, 4, 5])
    floor_print(root)
    # codec.deserialize(codec.serialize(root))
    sres = codec.serialize(root)
    print(sres)
