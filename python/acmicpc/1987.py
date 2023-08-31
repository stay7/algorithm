"""
2021-08-26
1987. 알파벳
"""
import sys


def bfs(pos):
    global max_count
    x, y = pos
    queue = set([(pos, board[x][y])])

    while queue:
        cur, path = queue.pop()
        x, y = cur

        if len(path) > max_count:
            max_count = len(path)

        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] not in path:
                    queue.add(((nx, ny), path + board[nx][ny]))


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_count = 1
bfs((0, 0))
print(max_count)
