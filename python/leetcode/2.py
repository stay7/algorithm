"""
2020-02-21
[leetcode](https://leetcode.com/problems/add-two-numbers/)
2. Add Two Numbers
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printListNode(self: ListNode):
    out = []
    while self:
        out.append(self.val)
        self = self.next
    print(out)


# 최초 풀이 후 최적화..!
# Runtime 60 ms (96.55%)
# Memory 14.4 MB (45.04%)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode()
        carry = 0

        while l1 or l2 or carry:
            cur.next = ListNode()
            cur = cur.next

            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = (sum) // 10
            cur.val = sum % 10

        return head.next


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    printListNode(Solution().addTwoNumbers(l1, l2))

    l1 = ListNode(0)
    l2 = ListNode(0)
    printListNode(Solution().addTwoNumbers(l1, l2))

    l1 = ListNode(9, ListNode(9, ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    printListNode(Solution().addTwoNumbers(l1, l2))
