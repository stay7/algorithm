"""
2021-08-17
1931. 회의실 배정
"""

import sys

N = int(sys.stdin.readline().rstrip())
meetings = []
for _ in range(N):
    S, E = map(int, sys.stdin.readline().split())
    meetings.append((E, S))

start = end = count = 0
meetings.sort()

for E, S in meetings:
    if S >= end:
        start, end = S, E
        count += 1
print(count)
