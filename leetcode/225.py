"""
2021-02-28
[leetcode](https://leetcode.com/problems/implement-stack-using-queues/)
225. Implement Stack using Queues
"""


# Runtime 28 ms (81.51%)
# Memory 14.2 MB (76.48%)
class MyStack:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        for i in range(len(self.list) - 1):
            out = self.list.pop(0)
            self.list.append(out)
        return self.list.pop(0)

    def top(self) -> int:
        return self.list[-1]

    def empty(self) -> bool:
        return len(self.list) == 0


if __name__ == "__main__":
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.top())
    print(myStack.pop())
    print(myStack.empty())
