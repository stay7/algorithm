class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        while self:
            print(self.val, end=' ')
            self = self.next
        print()


def sum_list(n1: ListNode, n2: ListNode):
    carry = 0
    result = head = ListNode()

    while n1 or n2:
        value = carry
        if n1:
            value += n1.val
            n1 = n1.next
        if n2:
            value += n2.val
            n2 = n2.next
        carry = value // 10
        result.next = ListNode(value % 10)
        result = result.next

    if carry:
        result.next = ListNode(1)

    return head.next


def sum_list_forward(n1: ListNode, n2: ListNode):
    stack1 = []
    stack2 = []
    stack_result = []
    carry = 0
    head = result = ListNode()

    while n1 or n2:
        if n1:
            stack1.append(n1.val)
            n1 = n1.next
        if n2:
            stack2.append(n2.val)
            n2 = n2.next

    while stack1 or stack2:
        value = carry
        if stack1:
            value += stack1.pop()
        if stack2:
            value += stack2.pop()
        carry = value // 10
        stack_result.append(value % 10)

    while stack_result:
        result.next = ListNode(stack_result.pop() % 10)
        result = result.next

    return head.next


if __name__ == "__main__":
    node_a = ListNode(9, ListNode(9, ListNode(9)))
    node_b = ListNode(5, ListNode(9, ListNode(2)))
    sum_list(node_a, node_b).print()
    node_a = ListNode(6, ListNode(1, ListNode(7)))
    node_b = ListNode(2, ListNode(9, ListNode(5, ListNode(1))))
    sum_list_forward(node_a, node_b).print()
