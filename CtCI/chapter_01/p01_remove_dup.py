class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        while self:
            print(self.val)
            self = self.next


def remove_dups(node: ListNode):
    numbers = {}
    head = prev = node

    while node:
        if node.val in numbers:
            prev.next = node.next
        else:
            numbers[node.val] = 1
            prev = node
        node = node.next
    return head


if __name__ == "__main__":
    nodes = ListNode(1, ListNode(3, ListNode(
        5, ListNode(3, ListNode(6, ListNode(1))))))
    result = remove_dups(nodes)
    result.print()
