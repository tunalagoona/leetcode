"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        start_node = ListNode(0)
        start_node.next = head
        length = 0
        elem = head

        while elem is not None:
            length += 1
            elem = elem.next
        pos = length - n + 1

        elem = start_node
        count = 1
        while True:
            if count == pos:
                elem.next = elem.next.next
                break
            elem = elem.next
            count += 1
        return start_node.next
