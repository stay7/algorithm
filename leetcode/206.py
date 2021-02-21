"""
2021-02-20
[leetcode](https://leetcode.com/problems/reverse-linked-list/)
206. Reverse Linked List
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        val = self.val
        nextVal = None
        if self.next:
            nextVal = self.next.val
        print(val, '->', nextVal)


def printListNode(head: ListNode):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    print(out)


# 최초 풀이
# Runtime 36 ms (69.43%)
# Memory 15.6 MB (78.79%)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    printListNode(Solution().reverseList(head))
