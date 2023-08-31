"""
2021-02-23
[leetcode](https://leetcode.com/problems/odd-even-linked-list/)
328. Odd Even Linked List
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


# 계속 멘탈 터지다가 처음으로 종이에 적고 한 번에 풀어내 문제
# 속도 메모리 모두 엄청나다...ㅎ
# Runtime 24 ms, (99.96%)
# Memory 16.1 MB, (98.18%)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        root_even = even = ListNode()
        root_odd = odd = ListNode()
        while head:
            odd.next, even.next = head, head.next
            odd, even = odd.next, even.next
            if not even:
                break
            head = even.next
        odd.next = root_even.next
        return root_odd.next


if __name__ == "__main__":
    head = ListNode(2, ListNode(1, ListNode(
        3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    Solution().oddEvenList(head).print()
