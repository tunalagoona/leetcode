"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time complexity: O(n)
# space complexity: O(1)
def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    depth = 1
    depth += max(max_depth(root.left), max_depth(root.right))
    return depth
