"""
2021-08-13
11729. 하노이 탑 이동 순서
"""

import sys


def hanoi(N, source, to, via):
    if N == 1:
        return path.append((source, to))

    hanoi(N-1, source, via, to)
    path.append((source, to))
    hanoi(N-1, via, to, source)


N = int(input())
path = []

hanoi(N, 1, 3, 2)

print(len(path))
for source, to in path:
    sys.stdout.write("{} {}\n".format(source, to))
