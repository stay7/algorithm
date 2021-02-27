"""
2021-02-24
[leetcode](https://leetcode.com/problems/reverse-linked-list-ii/)
92. Reverse Linked List II
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        out = []
        while self:
            out.append(self.val)
            self = self.next
        print(out)


# O(N)에 풀려고 노력한 문제
# Runtime 32 ms, (66.24%)
# Memory 14.3 MB, (90.85%)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        index = 1
        root = ListNode()
        root.next = head
        root_left = prev = root

        while head and index <= right:
            next = head.next
            if index == left:
                root_left = prev
            if left < index and index <= right:
                head.next = prev
            prev, head = head, next
            index += 1
        root_left.next.next = head
        root_left.next = prev
        return root.next


if __name__ == "__main__":
    head = ListNode(5)
    left, right = 1, 1
    Solution().reverseBetween(head, left, right).print()
