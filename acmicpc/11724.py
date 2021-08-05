"""
2021-08-05
11724. 연결 요소의 개수
"""
import sys
import collections


def dfs(start):
    stack = [start]
    visit.add(start)

    while stack:
        cur = stack.pop()
        for node in graph[cur]:
            if node not in visit:
                stack.append(node)
                visit.add(node)


V, E = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)

for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visit = set()
for i in range(1, V+1):
    if i not in visit:
        dfs(i)
        count += 1
sys.stdout.write(str(count)+'\n')
