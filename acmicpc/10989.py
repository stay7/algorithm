"""
2021-07-28
10989. 수 정렬하기 3
"""

import sys

N = int(sys.stdin.readline())
counts = [0 for _ in range(10001)]

for _ in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(1, 10001):
    for count in range(counts[i]):
        sys.stdout.write('{}\n'.format(i))
