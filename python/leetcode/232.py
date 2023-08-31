"""
2021-03-01
[leetcode](https://leetcode.com/problems/implement-queue-using-stacks/submissions/)
232. Implement Queue using Stacks
"""


# Runtime 32 ms(54.01%)
# Memory 14.3 MB(74.73%)
class MyQueue:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        temp = []
        while self.list:
            out = self.list.pop()
            temp.append(out)
        key = temp.pop()
        while temp:
            self.list.append(temp.pop())
        return key

    def peek(self) -> int:
        return self.list[0]

    def empty(self) -> bool:
        return len(self.list) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)  # queue is: [1]
    myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek()  # return 1
    myQueue.pop()  # return 1, queue is [2]
    myQueue.empty()  # return false
