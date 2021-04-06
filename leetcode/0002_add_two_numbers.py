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


e3 = ListNode(3)
e2 = ListNode(4, e3)
e1 = ListNode(2, e2)

d3 = ListNode(9)
d2 = ListNode(6, d3)
d1 = ListNode(5, d2)

s = Solution()
root = s.addTwoNumbers(e1, d1)
print(root.val)
print(root.next.val)
print(root.next.next.val)
print(root.next.next.next.val)
