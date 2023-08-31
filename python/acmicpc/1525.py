"""
2021-08-24
1525. 퍼즐
"""

import collections


def bfs(start):
    out = []
    queue = collections.deque()
    status = ''.join(graph)
    queue.append((start, status, 0))
    visit = set([status])

    while queue:
        cur, puzzle, count = queue.popleft()

        if puzzle == '123456780':
            out.append(count)

        # UP
        if cur > 2:
            status = list(puzzle)
            status[cur], status[cur-3] = status[cur-3], status[cur]
            status = ''.join(status)
            if status not in visit:
                queue.append((cur-3, status, count+1))
                visit.add(status)

        # DOWN
        if cur < 6:
            status = list(puzzle)
            status[cur], status[cur+3] = status[cur+3], status[cur]
            status = ''.join(status)
            if status not in visit:
                queue.append((cur+3, status, count+1))
                visit.add(status)

        # RIGHT
        if cur % 3 != 2:
            status = list(puzzle)
            status[cur], status[cur+1] = status[cur+1], status[cur]
            status = ''.join(status)
            if status not in visit:
                queue.append((cur+1, status, count+1))
                visit.add(status)

        # LEFT
        if cur % 3 != 0:
            status = list(puzzle)
            status[cur], status[cur-1] = status[cur-1], status[cur]
            status = ''.join(status)
            if status not in visit:
                queue.append((cur-1, status, count+1))
                visit.add(status)
    if len(out) > 0:
        return min(out)
    return -1


graph = []
pos = (0, 0)
for i in range(3):
    line = input().split()
    for j in range(3):
        graph.append(line[j])
        if line[j] == '0':
            pos = i*3 + j

print(bfs(pos))
