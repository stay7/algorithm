"""
2021-08-06
10451. 순열 사이클
"""

import collections


def dfs(start):
    for node in graph[start]:
        if node not in visit:
            visit.add(node)
            dfs(node)


TC = int(input())
for _ in range(TC):
    N = int(input())
    edges = list(map(int, input().split()))
    graph = collections.defaultdict(list)
    visit = set()
    count = 0

    for i, edge in enumerate(edges):
        graph[i+1].append(edge)

    for i in range(1, N+1):
        if i not in visit:
            visit.add(i)
            dfs(i)
            count += 1
    print(count)
