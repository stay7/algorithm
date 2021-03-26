"""
2021-03-26
[leetcode](https://leetcode.com/problems/merge-k-sorted-lists/)
23. Merge k Sorted Lists
"""

from typing import List


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


# priority queue 문제 -> 힙을 써라!.
# 이 문제는 heap을 쓰지 않고 풀었음.. -> 매우 느림
# Runtime 5524 ms (5.64%)
# Memory 17.6 MB (97.92%)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = cur = ListNode()

        while True:
            [index, min] = selectMin(lists)
            if index == None:
                break
            lists[index] = lists[index].next
            if lists[index] == None:
                lists.pop(index)
            new = ListNode(min)
            cur.next = new
            cur = new
        return head.next


def selectMin(lists: List[ListNode]) -> List[int]:
    index = min = None
    for i in range(0, len(lists)):
        if lists[i] != None:
            index, min = i, lists[i].val
            break

    if index == None:
        return [None, None]

    for i in range(index, len(lists)):
        if lists[i] == None:
            continue
        if min > lists[i].val:
            index, min = i, lists[i].val
    return [index, min]


if __name__ == "__main__":
    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(
        1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    Solution().mergeKLists(lists).print()
