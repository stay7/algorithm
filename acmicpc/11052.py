"""
2021-07-28
11052.카드 구매하기
"""

N = int(input())
prices = [0] + list(map(int, input().split()))

dp = [0, prices[1]]
for i in range(2, N+1):
    candidates = [prices[i]]
    for j in range(1, i//2 + 1):
        # print('p[{}] + p[{}]'.format(i-j, j))
        candidates.append(dp[i-j]+dp[j])
    dp.append(max(candidates))
print(dp[-1])
