"""
2021-08-19
9095. 1, 2, 3 더하기
"""

import sys

TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    N = int(sys.stdin.readline().rstrip())
    dp = [0, 1, 2, 4]
    for i in range(4, N+1):
        dp.append(dp[i-3]+dp[i-2]+dp[i-1])
    print(dp[N])
