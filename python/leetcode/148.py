"""
2021-04-30
[leetcode](https://leetcode.com/problems/sort-list/)
148. Sort List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Merge sort 직접 구현
# Runtime 544 ms (24.81%)
# Memory 50.9 MB (6.40%)
class Solution:
    def merge(self, l1: ListNode, l2: ListNode):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.merge(l1.next, l2)
        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        slow = fast = head
        while slow and fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)


# 제일 빠르면서 간단한 linked list -> python array
# Runtime 148ms (98.49%)
# Memory 30.1MB (89.02%)
class Solution1:
    def sortList(self, head: ListNode) -> ListNode:
        root = head
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.sort()

        head = root
        for num in nums:
            head.val = num
            head = head.next
        return root


if "__main__" == __name__:
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(Solution().sortList(head))
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    print(Solution().sortList(head))
    head = None
    print(Solution().sortList(head))
