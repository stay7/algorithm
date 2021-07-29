"""
2021-07-29
1406. 에디터
"""

import sys


class Node:
    def __init__(self, val='', prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


s = sys.stdin.readline().rstrip()
M = int(sys.stdin.readline())

head = prev = Node()
end = cur = Node()
for char in s:
    node = Node(char, prev)
    prev.next = node
    prev = node

cur.prev = prev
cur.prev.next = cur


for _ in range(M):
    line = sys.stdin.readline().split()
    if line[0] == 'L':
        if cur.prev != head:
            cur = cur.prev
    elif line[0] == 'D':
        if cur.next:
            cur = cur.next
    elif line[0] == 'B':
        if cur.prev != head:
            prev = cur.prev.prev
            cur.prev = prev
            prev.next = cur
    elif line[0] == 'P':
        node = Node(line[1], cur.prev, cur)
        cur.prev.next = node
        cur.prev = node

head = head.next
end.prev.next = None
out = []
while head:
    out.append(head.val)
    head = head.next
out.append('\n')
sys.stdout.write(''.join(out))
