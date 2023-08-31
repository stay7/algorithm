"""
2021-08-13
11726. 2×n 타일링 2
"""

dp = [1, 3]
N = int(input())
for i in range(2, N):
    dp.append(dp[i-1] + dp[i-2]*2)
print(dp[N-1] % 10007)
