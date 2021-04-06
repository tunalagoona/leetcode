"""
https://leetcode.com/problems/add-two-numbers/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        node = head
        memo = 0

        while l1 or l2 or memo:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            new_value = val1 + val2 + memo
            node.next = ListNode(new_value % 10)
            node = node.next
            memo = 1 if new_value > 9 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
