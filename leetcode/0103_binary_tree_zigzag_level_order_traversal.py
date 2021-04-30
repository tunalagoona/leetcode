"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#  O(n**2 * log(n)) time complexity
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        result.append([root.val])
        st = [root]
        left_to_right = False

        while len(st) > 0:
            level = []
            for _ in range(len(st)):
                node = st.pop(0)
                if node.left is not None:
                    st.append(node.left)
                    level.append(node.left.val)
                if node.right is not None:
                    st.append(node.right)
                    level.append(node.right.val)
            if not left_to_right:
                level.reverse()  # O(n)

            result.append(level)
            left_to_right = not left_to_right
        result.pop()
        return result
