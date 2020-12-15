"""
https://leetcode.com/problems/reverse-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        head = prev
        return head
