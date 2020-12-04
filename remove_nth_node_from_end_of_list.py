"""
Linked lists / easy
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
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


if __name__ == "__main__":
    num = 1

    # e5 = ListNode(5, None)
    # e4 = ListNode(4, e5)
    # e3 = ListNode(3, e4)
    # e2 = ListNode(2, e3)
    # e1 = ListNode(1, e2)
    e1 = ListNode(1, None)

    sol = Solution()
    sol.removeNthFromEnd(head=e1, n=num)
