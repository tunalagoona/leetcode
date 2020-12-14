"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# time complexity: O(1)
# space complexity: O(1)
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


