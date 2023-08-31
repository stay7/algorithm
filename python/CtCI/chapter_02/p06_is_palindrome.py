class ListNode:
    def __init__(self, val='', next=None):
        self.val = val
        self.next = next


def is_palindrome(node: ListNode):
    stack_char = []
    current = runner = node

    while runner and runner.next:
        stack_char.append(current.val)
        current = current.next
        runner = runner.next.next

    # odd
    if runner != None:
        current = current.next

    while current:
        if current.val != stack_char.pop():
            return False
        current = current.next

    return True


if __name__ == "__main__":
    node = ListNode('c', ListNode(
        'a', ListNode('t', ListNode('a', ListNode('c')))))
    node1 = ListNode('c', ListNode(
        'a', ListNode('t', ListNode('t', ListNode('a', ListNode('c'))))))

    print(is_palindrome(node))
    print(is_palindrome(node1))
