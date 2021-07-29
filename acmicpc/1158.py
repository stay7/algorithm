"""
2021-07-29
1158. 요세푸스 문제
"""

import sys


class Node:
    def __init__(self, val='0', next=None):
        self.val = val
        self.next = None


N, K = map(int, sys.stdin.readline().rstrip().split())
head = cur = Node()
out = []

for i in range(N):
    cur.next = Node(str(i+1))
    cur = cur.next
cur.next = head.next


step = 0
prev, cur = cur, cur.next
while len(out) < N:
    step += 1
    if step == K:
        out.append(cur.val)
        prev.next = cur.next
        step = 0
    prev, cur = cur, cur.next

sys.stdout.write('<{}>\n'.format(', '.join(out)))
