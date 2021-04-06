""""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        r = []
        if root:
            result = self.traverse(root, r)
            return result
        else:
            return r

    def traverse(self, node: TreeNode, res):
        if node:
            if node.left:
                self.traverse(node.left, res)
            res.append(node.val)
            if node.right:
                self.traverse(node.right, res)
        return res


# e4 = TreeNode(1, None, None)
# e5 = TreeNode(3, None, None)
# e2 = TreeNode(2, e4, e5)
# e6 = TreeNode(5, None, None)
# e7 = TreeNode(7, None, None)
# e3 = TreeNode(6, e6, e7)
# e1 = TreeNode(4, e2, e3)
e1 = TreeNode(1)
s = Solution()
print(s.inorderTraversal(e1))
