"""
2021-08-08
11047. 동전 0
"""
import sys
import bisect

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
count = 0

while K > 0:
    index = bisect.bisect_right(coins, K)-1
    quotient = K // coins[index]
    K -= coins[index] * quotient
    count += quotient
print(count)
