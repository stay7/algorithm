"""
2021-07-31
1934. 최소공배수
"""
import sys


def gcd(A, B):
    if B == 0:
        return A
    return gcd(B, A % B)


TC = int(sys.stdin.readline())
for _ in range(TC):
    A, B = map(int, sys.stdin.readline().split())
    if A < B:
        A, B = B, A
    sys.stdout.write('{}\n'.format(int(A*B/gcd(A, B))))
