"""
2020-02-18
[leetcode](https://leetcode.com/problems/palindrome-linked-list/)
234. Palindrome Linked List
"""


# 어렵지 않게 해결
# 러너 기법으로 한 번의 순회로도 해결할 수 있다
# Runtime 64 ms (90.58%)
# Memory 24.3 MB (79.73%)
class Solution:
    def isPalindrome(self, head) -> bool:
        cur = head
        routes = []
        while cur:
            routes.append(cur.val)
            cur = cur.next

        left, right = 0, len(routes)-1
        while left < right:
            if routes[left] != routes[right]:
                return False
            left, right = left + 1, right-1
        return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == "__main__":
    # head = ListNode(1, ListNode(2))
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(Solution().isPalindrome(head))
