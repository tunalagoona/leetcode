"""
Trees / easy
Time complexity O(n), Space complexity O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
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


if __name__ == "__main__":
    # nd1 = TreeNode(1, None, None)
    # nd2 = TreeNode(4, 3, 6)
    # root_nd = TreeNode(5, nd1, nd2)

    nd2 = TreeNode(4, None, None)
    nd4 = TreeNode(3, None, None)
    nd5 = TreeNode(7, None, None)
    nd3 = TreeNode(6, nd4, nd5)
    root_nd = TreeNode(5, nd2, nd3)

    sol = Solution()
    sol.isValidBST(root_nd)
