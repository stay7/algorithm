"""
2021-08-06
10451. 순열 사이클
"""

import collections


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
            stack = [i]
            while stack:
                cur = stack.pop()
                visit.add(i)
                for node in graph[cur]:
                    if node not in visit:
                        stack.append(node)
                        visit.add(node)
            count += 1
    print(count)
