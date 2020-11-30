# level: easy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == "__main__":
    my_list = [1, 4, 9, 5]

    linked_list = []
    e1 = ListNode(1)
    e2 = ListNode(4)
    e1.next = e2
    e3 = ListNode(9)
    e2.next = e3
    e4 = ListNode(5)
    e3.next = e4

    print(delete_node(e2))

