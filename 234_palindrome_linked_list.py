"""
https://leetcode.com/problems/palindrome-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        memo = []
        while head is not None:
            memo.append(head.val)
            head = head.next

        length = len(memo)
        mid = length // 2
        a = memo[:mid]
        a.reverse()
        if length % 2 == 0:
            return True if a == memo[mid:] else False
        else:
            return True if a == memo[mid + 1:] else False
