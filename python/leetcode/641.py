"""
2021-03-26
[leetcode](https://leetcode.com/problems/design-circular-deque/)
641. Design Circular Deque
"""


# 처음 head와 tail의 위치는 중요하다
# Runtime 72 ms (60.11%)
# Memory 15.7 MB (8.65%)
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val


class MyCircularDeque:

    def __init__(self, k: int):
        if k == 0:
            return
        head = tail = ListNode()
        for _ in range(k):
            new = ListNode()
            tail.next = new
            new.prev = tail
            tail = new
        head.prev, tail.next = tail, head
        self.head, self.tail = head, head.next
        self.size, self.len = 0, k

    def insertFront(self, value: int) -> bool:
        if self.size >= self.len:
            return False
        self.head.val = value
        self.head = self.head.prev
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size >= self.len:
            return False
        self.tail.val = value
        self.tail = self.tail.next
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size <= 0:
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size <= 0:
            return False
        self.tail = self.tail.prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.len


if __name__ == "__main__":
    circularDeque = MyCircularDeque(5)
    print(circularDeque.insertFront(7))			# return true
    print(circularDeque.insertLast(0))			# return true
    print(circularDeque.getFront())			# return true
    print(circularDeque.insertLast(3))			# return false, the queue is full
    print(circularDeque.getFront())
    print(circularDeque.insertFront(9))			# return false, the queue is full
    print(circularDeque.getRear())
    print(circularDeque.getFront())
    print(circularDeque.getFront())
    print(circularDeque.deleteLast())
    print(circularDeque.getRear())
    # print(circularDeque.getRear())  			# return 2
    # print(circularDeque.isFull())				# return true
    # print(circularDeque.deleteLast())			# return true
    # print(circularDeque.insertFront(4))			# return true
    # print(circularDeque.getFront())			# return 4
