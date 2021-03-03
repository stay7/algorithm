"""
2021-03-02
[leetcode](https://leetcode.com/problems/design-circular-queue/)
622. Design Circular Queue
"""

# 예전 자료구조 시간에 한 기억이 떠오른다..!
# Runtime 68 ms (74.63%)
# Memory 14.9 MB (49.31%)


class MyCircularQueue:

    def __init__(self, k: int):
        self.len = 0
        self.list = [-1]*k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.len == len(self.list):
            return False

        self.list[self.tail] = value
        self.tail += 1
        self.len += 1
        if self.tail == len(self.list):
            self.tail = 0
        return True

    def deQueue(self) -> bool:
        if self.len == 0:
            return False

        self.list[self.head] = -1
        self.head += 1
        self.len -= 1
        if self.head == len(self.list):
            self.head = 0
        return True

    def Front(self) -> int:
        if self.len == 0:
            return -1
        return self.list[self.head]

    def Rear(self) -> int:
        if self.len == 0:
            return -1
        lastIndex = (self.head + self.len - 1) % len(self.list)
        return self.list[lastIndex]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == len(self.list)


if __name__ == "__main__":
    k = 3
    myCircularQueue = MyCircularQueue(k)
    print(myCircularQueue.enQueue(1))  # return True
    print(myCircularQueue.enQueue(2))  # return True
    print(myCircularQueue.enQueue(3))  # return True
    print(myCircularQueue.enQueue(4))  # return False
    print(myCircularQueue.Rear())  # return 3
    print(myCircularQueue.isFull())  # return True
    print(myCircularQueue.deQueue())  # return True
    print(myCircularQueue.enQueue(4))  # return True
    print(myCircularQueue.Rear())  # return 4
