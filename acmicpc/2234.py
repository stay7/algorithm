"""
2021-10-08
2234. 성곽
"""

import collections


def bfs(start, id):
    room_size = 0
    queue = collections.deque([start])
    while queue:
        x, y = queue.popleft()
        room_id[x][y] = id
        room_size += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (1 << k) & graph[x][y] == 0 and (nx, ny) not in visit:
                queue.append((nx, ny))
                visit.add((nx, ny))
    return room_size


def find_neighbor(start, id):
    queue = collections.deque([start])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < len(room_id) and 0 <= ny < len(room_id[0]):
                if room_id[nx][ny] != id:
                    merge_sizes.append(sizes[id - 1] + sizes[room_id[nx][ny] - 1])
                    continue
                if (nx, ny) not in visit:
                    queue.append((nx, ny))
                    visit.add((nx, ny))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

room_id = [[0] * N for _ in range(M)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

sizes = []
count = 0
merge_sizes = []

visit = set()
for i in range(M):
    for j in range(N):
        if (i, j) not in visit:
            visit.add((i, j))
            count += 1
            sizes.append(bfs((i, j), count))

visit.clear()
neighbor = set()
for i in range(M):
    for j in range(N):
        if (i, j) not in visit:
            visit.add((i, j))
            find_neighbor((i, j), room_id[i][j])

print(count)
print(max(sizes))
print(max(merge_sizes))
