"""
2021-08-07
11725. 트리의 부모 찾기
"""

import sys
import collections


def dfs(parent, cur):
    stack = []
    stack.append((parent, cur))
    parents[cur] = parent
    visit.add(cur)

    while stack:
        parent, cur = stack.pop()

        for node in graph[cur]:
            if node not in visit:
                stack.append((cur, node))
                parents[node] = cur
                visit.add(node)


N = int(input())
graph = collections.defaultdict(list)

for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

parents = [0] * (N+1)
visit = set()
dfs(1, 1)
for i in range(2, len(parents)):
    sys.stdout.write('{}\n'.format(parents[i]))
