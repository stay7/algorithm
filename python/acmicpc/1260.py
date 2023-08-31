"""
2021-08-05
1260. DFS와 BFS
"""
import sys
import collections


def dfs(start):
    visit.add(start)
    out_dfs.append(str(start))
    for i in graph[start]:
        if i not in visit:
            dfs(i)


def bfs(start):
    queue = collections.deque()
    queue.append(start)
    visit.add(start)

    while queue:
        cur = queue.popleft()
        out_bfs.append(str(cur))
        for i in graph[cur]:
            if i not in visit:
                queue.append(i)
                visit.add(i)


V, E, S = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)

for _ in range(E):
    start, dest = map(int, sys.stdin.readline().split())
    graph[start].append(dest)
    graph[dest].append(start)

for i in range(1, V+1):
    graph[i].sort()

# DFS
visit = set()
out_dfs = []
dfs(S)

visit = set()
out_bfs = []
bfs(S)


sys.stdout.write('{}\n'.format(' '.join(out_dfs)))
sys.stdout.write('{}\n'.format(' '.join(out_bfs)))
