"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            start = l1
            l1 = l1.next
        else:
            start = l2
            l2 = l2.next
        s = start

        while l1 is not None or l2 is not None:
            if l1 is None:
                start.next = l2
                start = l2
                l2 = l2.next
            elif l2 is None:
                start.next = l1
                start = l1
                l1 = l1.next
            else:
                if l2.val <= l1.val:
                    start.next = l2
                    start = start.next
                    l2 = l2.next
                elif l2.val > l1.val:
                    start.next = l1
                    start = start.next
                    l1 = l1.next
        return s
