class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        while self:
            print(self.val, end=' ')
            self = self.next
        print(end='\n')


def partiton_list(node: ListNode, partition: int):
    less = cur_less = ListNode()
    more = cur_more = ListNode()

    while node:
        if node.val < partition:
            cur_less.next = node
            cur_less = cur_less.next
        else:
            cur_more.next = node
            cur_more = cur_more.next
        node = node.next

    cur_less.next = more.next
    cur_more.next = None
    return less.next


if __name__ == "__main__":
    node = ListNode(3, ListNode(5, ListNode(
        8, ListNode(5, ListNode(10, ListNode(2, ListNode(1)))))))
    partiton_list(node, 5).print()
