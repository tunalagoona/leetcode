"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time complexity
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal idx
            if left > right:
                return None

            node = TreeNode(preorder[idx])
            idx += 1

            node.left = helper(left, inorder.index(node.val) - 1)
            node.right = helper(inorder.index(node.val) + 1, right)

            return node

        idx = 0
        root = helper(0, len(preorder) - 1)

        return root
