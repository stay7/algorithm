"""
2021-08-21
11657. 타임머신
"""

import sys
import collections


def bellman(src):
    upper = [float('inf') for _ in range(N+1)]
    upper[src] = 0

    for _ in range(N):
        updated = False
        for cur in range(1, N+1):
            for dest, cost in graph[cur].items():
                if upper[dest] > upper[cur] + cost:
                    upper[dest] = upper[cur] + cost
                    updated = True
        if not updated:
            break
    if updated:
        return -1
    return upper


N, M = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(dict)

for _ in range(M):
    src, dest, time = map(int, sys.stdin.readline().split())
    if dest in graph[src]:
        graph[src][dest] = min(graph[src][dest], time)
    else:
        graph[src][dest] = time

upper = bellman(1)
if upper == -1:
    print(upper)
else:
    upper = [-1 if x == float('inf') else x for x in upper]
    for i in range(2, N+1):
        print(upper[i])
