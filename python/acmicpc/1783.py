"""
2021-08-10
1783. 병든 나이트
"""


def count_step(N, M):
    if N == 1:
        return 1
    if N == 2:
        return min(4, (M-1) // 2 + 1)
    if M < 7:
        return min(4, M)
    return M-2


N, M = map(int, input().split())
print(count_step(N, M))
