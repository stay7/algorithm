"""
2021-08-03
11005. 진법 변화
"""
import sys

N, B = map(int, sys.stdin.readline().split())
digits = []
while N > 0:
    digits.append(N % B)
    N //= B
digits.reverse()

for digit in digits:
    out = str(digit)
    if digit > 9:
        out = chr(ord('A') + (digit-10))
    sys.stdout.write(out)
sys.stdout.write('\n')
