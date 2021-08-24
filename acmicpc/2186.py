"""
2021-08-24
2186. 문자판
"""

import sys


def dfs(pos, index):
    if index == len(word):
        return 1

    x, y = pos
    if dp[x][y][index] != -1:
        return dp[x][y][index]

    count = 0
    for i in range(4):
        temp_x, temp_y = x, y
        for _ in range(K):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == word[index]:
                    count += dfs((nx, ny), index+1)
            temp_x, temp_y = nx, ny
    dp[x][y][index] = count
    return dp[x][y][index]


dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

N, M, K = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
word = sys.stdin.readline().rstrip()

dp = [[[-1] * len(word) for _ in range(M)] for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == word[0]:
            count += dfs((i, j), 1)
print(count)
