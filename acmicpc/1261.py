"""
2021-08-21
1261. 알고스팟
"""
import sys
import heapq


def dijkstra(x, y):
    dist = [[float('inf') for _ in range(M)] for _ in range(N)]
    dist[x][y] = 0
    pq = []
    heapq.heappush(pq, (0, (x, y)))
    while pq:
        cost, (x, y) = heapq.heappop(pq)
        if cost > dist[x][y]:
            continue

        # up
        if x > 0:
            next_dist = cost + int(graph[x-1][y])
            if next_dist < dist[x-1][y]:
                dist[x-1][y] = next_dist
                heapq.heappush(pq, (next_dist, (x-1, y)))
        # down
        if x < N-1:
            next_dist = cost + int(graph[x+1][y])
            if next_dist < dist[x+1][y]:
                dist[x+1][y] = next_dist
                heapq.heappush(pq, (next_dist, (x+1, y)))

        # left
        if y > 0:
            next_dist = cost + int(graph[x][y-1])
            if next_dist < dist[x][y-1]:
                dist[x][y-1] = next_dist
                heapq.heappush(pq, (next_dist, (x, y-1)))

        # right
        if y < M-1:
            next_dist = cost + int(graph[x][y+1])
            if next_dist < dist[x][y+1]:
                dist[x][y+1] = next_dist
                heapq.heappush(pq, (next_dist, (x, y+1)))
    return dist


M, N = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

dist = dijkstra(0, 0)
print(dist[N-1][M-1])
