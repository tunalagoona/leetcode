# level: easy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    depth = 1
    depth += max(max_depth(root.left), max_depth(root.right))
    print(depth)
    return depth


if __name__ == "__main__":
    e1 = TreeNode(val=9, left=None, right=None)
    e3 = TreeNode(val=15, left=None, right=None)
    e4 = TreeNode(val=7, left=None, right=None)
    e2 = TreeNode(val=20, left=e3, right=e4)
    tree_root = TreeNode(val=3, left=e1, right=e2)

    # e1 = TreeNode(val=2, left=None, right=None)
    # tree_root = TreeNode(val=1, left=None, right=e1)

    max_depth(tree_root)
