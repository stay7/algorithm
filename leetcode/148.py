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


# 제일 빠르면서 간단한 linked list -> python array
# Runtime 148ms (98.49%)
# Memory 30.1MB (89.02%)
class Solution:
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
