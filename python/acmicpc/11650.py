"""
2021-07-28
11650.좌표 정렬하기
"""

import sys
N = int(sys.stdin.readline())
points = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.sort(key=lambda point: (point[0], point[1]))
for point in points:
    x, y = point
    sys.stdout.write('{} {}\n'.format(x, y))
