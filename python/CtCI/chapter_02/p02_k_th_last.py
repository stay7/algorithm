class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


# 처음에 작성한 코드
def k_th_last(node: ListNode, k: int):
    slow_index = fast_index = 1
    slow = fast = node
    length = 0
    while fast and fast.next:
        fast = fast.next.next
        fast_index += 2
        slow = slow.next
        slow_index += 1

    if fast is None:
        length = fast_index - 1
    else:
        length = fast_index

    target = length - k

    if slow_index > target:
        slow, slow_index = node, 1
    while slow_index <= target:
        slow = slow.next
        slow_index += 1
    return slow.val


# optimal한 코드
# 길이 l인 경우 runner를 k만큼 보내고
# runner가 None에 도달할 때 까지 current를 이동 (l-k+1)
def kth_to_last(ll, k):
    runner = current = ll
    for _ in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current.val


if __name__ == "__main__":
    node = ListNode(1, ListNode(3, ListNode(
        5, ListNode(7, ListNode(9, ListNode(10))))))

    print(k_th_last(node, 6))
    print(kth_to_last(node, 6))
