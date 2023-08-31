"""
2021-08-20
10971. 외판원 순회 2
"""
import sys


def dfs(start, cur, cost, visits):
    if len(visits) == N:
        if graph[cur][start] != 0:
            out.append(cost + graph[cur][start])
        return

    for i, dist in enumerate(graph[cur]):
        if dist != 0 and i not in visits:
            visits.add(i)
            dfs(start, i, cost+dist, visits)
            visits.remove(i)


N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
out = []

for i in range(N):
    dfs(i, i, 0, set([i]))
print(min(out))
