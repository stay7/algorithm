"""
2021-09-10
15486. 퇴사 2
"""

import sys

N = int(sys.stdin.readline().rstrip())
jobs = [[] for _ in range(N + 1)]
dp = [0] * (N + 1)

for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    if i + t <= N:
        jobs[i + t].append((p, i + 1))


for i in range(1, N + 1):
    done_jobs = jobs[i]
    dp[i] = dp[i - 1]
    earnings = []
    for pay, idx in done_jobs:
        earnings.append(dp[idx - 1] + pay)
    if earnings:
        dp[i] = max(max(earnings), dp[i])
print(dp[-1])
