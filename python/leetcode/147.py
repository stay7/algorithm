"""
2021-05-03
[leetcode](https://leetcode.com/problems/insertion-sort-list/)
147. Insertion Sort List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 연결리스트의 삽입 정렬
# Runtime 172 ms (87.23%)
# Memory 16.2 MB (97.41%)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next

            # 이 한 줄이 1932ms -> 172ms
            # 처음으로 돌아가야하는 경우에만 돌아가기
            if head and cur.val > head.val:
                cur = parent
        return parent.next


if "__main__" == __name__:
    Solution()
