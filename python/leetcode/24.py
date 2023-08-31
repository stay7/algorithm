"""
2021-02-22
[leetcode](https://leetcode.com/problems/swap-nodes-in-pairs/)
24. Swap Nodes in Pairs
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


# 풀면서 현타 최소 2번
# Runtime 32 ms (61.86%)
# Memory 14.2 MB (52.88%)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            prev.next = b

            prev = head
            head = head.next
        return root.next


if __name__ == "__main__":
    head = ListNode()
    Solution().swapPairs(head).print()
