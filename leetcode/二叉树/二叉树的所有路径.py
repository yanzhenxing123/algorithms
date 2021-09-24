"""
@Author: yanzx
@Date: 2020/12/7 14:49
@Description: 
"""
from createTree import createTree


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # 建立两个全局变量
        path = ""
        result = []
        # 另建一个helper函数，方便对全局变量path,result的使用
        self.helper(root, path, result)
        return result

    # void型函数，给结果列表result中添加由path为前缀的所有路径
    def helper(self, root, path, result):

        if root is None:
            return
        path = path + str(root.val)

        # 递归对左孩子求路径
        if root.left:
            self.helper(root.left, path + "->", result)
        # 递归对右孩子求路径
        if root.right:
            self.helper(root.right, path + "->", result)
        # 如果是叶子，加入result
        if root.left is None and root.right is None:
            result.append(path)
        # Write your code here



if __name__ == '__main__':
    items = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = TreeNode(items[0])
    createTree(root, items)
    s = Solution()
    res = s.binaryTreePaths(root)
    print(res)
