"""
2021-08-08
1654. 랜선 자르기
"""
import sys


def check(len):
    sum = 0
    for wire in wires:
        sum += wire//len
    return sum


K, N = map(int, sys.stdin.readline().split())

wires = []
for _ in range(K):
    wires.append(int(sys.stdin.readline()))

left, right = 1, sum(wires)//N+1
while left < right:
    mid = left + (right-left)//2
    if left == mid:
        break
    result = check(mid)
    if result < N:
        right = mid
    else:
        left = mid
print(left)
