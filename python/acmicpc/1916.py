"""
2021-08-21
1916. 최소비용 구하기
"""

import sys
import collections
import heapq


def dijkstra(src: int):
    dist = [float('inf') for _ in range(N+1)]
    dist[src] = 0
    pq = []
    heapq.heappush(pq, (0, src))
    while pq:
        cost, cur = heapq.heappop(pq)
        if cost > dist[cur]:
            continue

        for v, v_dist in graph[cur].items():
            v_cost = cost + v_dist
            if v_cost < dist[v]:
                heapq.heappush(pq, (v_cost, v))
                dist[v] = v_cost
    return dist


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = collections.defaultdict(dict)
for _ in range(M):
    src, dest, cost = map(int, sys.stdin.readline().split())
    if dest not in graph[src]:
        graph[src][dest] = cost
    else:
        graph[src][dest] = min(graph[src][dest], cost)

src, dest = map(int, sys.stdin.readline().split())

dist = dijkstra(src)
print(dist[dest])
