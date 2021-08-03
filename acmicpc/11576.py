"""
2021-08-04
11576. Base Conversion
"""

A, B = map(int, input().split())
m = int(input())
num = 0
out = []

digits = input().split()
for i, digit in enumerate(digits):
    num += int(digit)*(A**(m-i-1))

while num:
    out.append(str(num % B))
    num //= B

out.reverse()
print(' '.join(out))
