class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_length_and_tail(node: ListNode):
    length = 0
    prev = node
    while node:
        length += 1
        prev = node
        node = node.next
    return length, prev


def intersection(n1: ListNode, n2: ListNode):
    len_1, tail_1 = get_length_and_tail(n1)
    len_2, tail_2 = get_length_and_tail(n2)

    if tail_1 is not tail_2:
        return False

    long, short = n1, n2
    if len_1 < len_2:
        long, short = short, long

    for _ in range(abs(len_1-len_2)):
        long = long.next

    while long is not short:
        long = long.next
        short = short.next

    return long


if __name__ == "__main__":
    head = ListNode(1, ListNode(3, ListNode(5)))
    print(intersection(head, head.next).val)  # 3
