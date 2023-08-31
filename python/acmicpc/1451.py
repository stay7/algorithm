"""
2021-08-19
1451. 직사각형으로 나누기
"""


import sys


def sector_sum(x, y, N, M):
    out = 0
    key = '{},{},{},{}'.format(x, y, N, M)
    if key in cache:
        return cache[key]
    for i in range(x, x+N):
        for j in range(y, y+M):
            out += nums[i][j]
    cache[key] = out
    return out


def split(x, y, N, M):
    multi = []

    for h in range(1, N+1):
        multi.append(sector_sum(x, y, h, M) *
                     sector_sum(x+h, y, N-h, M))

    for w in range(1, M+1):
        multi.append(sector_sum(x, y, N, w) *
                     sector_sum(x, y+w, N, M-w))
    # print(multi)
    return max(multi)


N, M = map(int, input().split())

nums = []
out = []
cache = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    nums.append([int(char) for char in word])

for h in range(1, N+1):
    out.append(split(0, 0, h, M)*sector_sum(h, 0, N-h, M))
    out.append(split(h, 0, N-h, M)*sector_sum(0, 0, h, M))

for w in range(1, M+1):
    out.append(split(0, 0, N, w)*sector_sum(0, w, N, M-w))
    out.append(split(0, w, N, M-w)*sector_sum(0, 0, N, w))


print(max(out))
