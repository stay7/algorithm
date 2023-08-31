"""
2021-08-04
11653. 소인수분해
"""
import sys
N = int(sys.stdin.readline().rstrip())

divisor = 2
while N > 1:
    if N % divisor == 0:
        N //= divisor
        sys.stdout.write('{}\n'.format(divisor))
    else:
        divisor += 1
