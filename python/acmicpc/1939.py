"""
2021-09-05
1939. 중량제한
"""

import heapq


def dijkstra(start, end):
    pq = []
    cost = [float("inf") for _ in range(N)]
    heapq.heappush(pq, (0, start))

    while pq:
        weight, cur = heapq.heappop(pq)


N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B, weight = map(int, input().split())
    if B in graph[A] and weight < graph[A][B]:
        continue
    graph[A][B] = weight
    graph[B][A] = weight

src, dest = map(int, input().split())
out = []
print(dijkstra(src, dest))


"""
3 3
1 2 4
3 1 3
2 3 5
1 3
"""
