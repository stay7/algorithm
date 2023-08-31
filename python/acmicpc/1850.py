"""
2021-08-02
1850. 최대공약수
"""

import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


A, B = map(int, sys.stdin.readline().split())
if A < B:
    A, B = B, A
divisor = gcd(A, B)

for _ in range(divisor):
    sys.stdout.write('1')
sys.stdout.write('\n')
