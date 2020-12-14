"""
https://leetcode.com/problems/validate-binary-search-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def is_valid_bst(self, root: TreeNode) -> bool:
        return self.bst_checker(root_node=root)

    def bst_checker(self, root_node, max_val=float('inf'), min_val=float('-inf')):
        is_bst = True

        if not root_node:
            return is_bst

        if root_node.val <= min_val or root_node.val >= max_val:
            is_bst = False
            return is_bst

        if not self.bst_checker(root_node=root_node.left, max_val=root_node.val, min_val=min_val) or not\
                self.bst_checker(root_node=root_node.right, max_val=max_val, min_val=root_node.val):
            is_bst = False
        else:
            is_bst = True
        return is_bst
