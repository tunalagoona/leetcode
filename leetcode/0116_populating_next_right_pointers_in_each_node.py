"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# O(n) time complexity
class Solution:
    def connect(self, root: "Node") -> "Node":
        q = [root]
        while q:
            node = q.pop(0)
            if node and node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                q.append(node.left)
                q.append(node.right)
        return root
