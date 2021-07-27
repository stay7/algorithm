"""
2021-07-27
2133. 타일 채우기
"""


def sol():
    N = int(input())
    if N % 2 == 1:
        return 0
    memo = [0] * (N+1)
    memo[2] = 3
    for i in range(4, N+1, 2):
        memo[i] = memo[i-2] * memo[2] + 2
        for j in range(i-2, 2, -2):
            # j의 특수 케이스 2개를 배치
            memo[i] += memo[i-j] * 2
    return memo[N]


print(sol())
