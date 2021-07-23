"""
2021-07-23
10951. A+B - 4
"""

import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    A, B = map(int, line.split())
    print(A+B)
