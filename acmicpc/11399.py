"""
2021-08-17
11399. ATM
"""

N = int(input())
times = list(map(int, input().split()))
times.sort()

time_sum = 0
for i in range(N):
    time_sum += (times[i]*(N-i))
print(time_sum)
