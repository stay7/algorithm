"""
2020-02-19
[leetcode](https://leetcode.com/problems/merge-two-sorted-lists/submissions/)
21. Trapping Rain Water
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 재귀를 생각하지 못해서 정말 긴 코드를 적고도 실패한 문제
# Runtime 36 ms(76.54%)
# Memory 14 MB (99.77%)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


def printList(list: ListNode):
    head = list
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    sol = Solution().mergeTwoLists(l1, l2)
    printList(sol)
