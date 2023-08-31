"""
2021-08-21
1238. 파티
"""

import sys
import collections
import heapq


def dijkstra(src, graph):
    dist = [float('inf') for _ in range(N+1)]
    dist[src] = 0
    pq = []
    heapq.heappush(pq, (0, src))
    while pq:
        cost, cur = heapq.heappop(pq)
        if dist[cur] < cost:
            continue
        for v, v_dist in graph[cur].items():
            v_cost = cost + v_dist
            if dist[v] > v_cost:
                dist[v] = v_cost
                heapq.heappush(pq, (v_cost, v))
    return dist


N, M, X = map(int, sys.stdin.readline().split())
adj = collections.defaultdict(dict)
reverse_adj = collections.defaultdict(dict)

for _ in range(M):
    src, dest, time = map(int, sys.stdin.readline().split())
    adj[src][dest] = time
    reverse_adj[dest][src] = time

to_home = dijkstra(X, adj)
to_party = dijkstra(X, reverse_adj)


max_cost = float('-inf')
for i in range(1, N+1):
    cost = to_home[i] + to_party[i]
    if cost > max_cost:
        max_cost = cost

print(max_cost)
