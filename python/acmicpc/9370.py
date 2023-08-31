"""
2021-10-08
9370. 미확인 도착지
"""

import sys
import heapq
import collections

input = sys.stdin.readline


def dijkstra(start):
    cost = [float("inf") for _ in range(N)]
    cost[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, cur = heapq.heappop(pq)

        if dist > cost[cur]:
            continue

        for nxt, nxt_dist in graph[cur]:
            if nxt_dist == 0:
                continue
            if nxt_dist + dist < cost[nxt]:
                cost[nxt] = nxt_dist + dist
                heapq.heappush(pq, (nxt_dist + dist, nxt))
    return cost


TC = int(input())
for _ in range(TC):
    out = []
    candidates = []
    N, M, T = map(int, input().split())  # 교차로, 도로, 목적지 후보의 개수
    S, G, H = map(int, input().split())
    graph = collections.defaultdict(list)

    for _ in range(M):
        a, b, d = map(int, input().split())
        if (a == G and b == H) or (a == H and b == G):
            d = d - 0.1
        graph[a - 1].append((b - 1, d))
        graph[b - 1].append((a - 1, d))

    for _ in range(T):
        candidates.append(int(input()))
    candidates.sort()

    costs = dijkstra(S - 1)
    for candidate in candidates:
        if type(costs[candidate - 1]) == float and costs[candidate - 1] != float("inf"):
            out.append(candidate)
    print(" ".join(list(map(str, out))))
