"""
2021-08-21
11404. 플로이드
"""
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[float('inf') for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    src, dest, cost = map(int, sys.stdin.readline().split())
    graph[src-1][dest-1] = min(graph[src-1][dest-1], cost)


for k in range(N):
    for i in range(N):
        if graph[i][k]:
            for j in range(N):
                graph[i][j] = min(
                    graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0
        graph[i][j] = str(graph[i][j])

for line in graph:
    print(' '.join(line))
