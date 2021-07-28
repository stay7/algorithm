"""
2021-07-28
10828. 스택
"""

import sys


class MyStack:
    def __init__(self):
        self.list = []

    def push(self, num: int):
        self.list.append(num)

    def pop(self):
        if not self.list:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write('{}\n'.format(self.list.pop()))

    def empty(self):
        if len(self.list) == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')

    def size(self):
        sys.stdout.write('{}\n'.format(len(self.list)))

    def top(self):
        if not self.list:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write('{}\n'.format(self.list[-1]))


PUSH, TOP, SIZE, EMPTY, POP = 'push', 'top', 'size', 'empty', 'pop'
stack = MyStack()
N = int(input())
for _ in range(N):
    line = sys.stdin.readline().split()
    command = line[0]
    if command == PUSH:
        stack.push(line[1])
    elif command == TOP:
        stack.top()
    elif command == SIZE:
        stack.size()
    elif command == EMPTY:
        stack.empty()
    elif command == POP:
        stack.pop()
