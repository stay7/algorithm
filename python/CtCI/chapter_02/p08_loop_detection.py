from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def circular_list(ll: ListNode):
    fast = slow = ll

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    fast = ll
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


if __name__ == "__main__":
    circular_head = ListNode(1)
    circular_head.next = ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, circular_head))))
    head = ListNode(9, ListNode(8, ListNode(
        7, ListNode(6, ListNode(3, circular_head)))))
    print(circular_list(head).val)
