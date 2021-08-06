"""
2021-08-06
1707. 이분 그래프
"""

import sys
import collections


TC = int(sys.stdin.readline())


for _ in range(TC):
    V, E = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)
    for _ in range(E):
        s, t = map(int, sys.stdin.readline().split())
        graph[s].append(t)
        graph[t].append(s)

    visit = [0 for _ in range(V+1)]
    queue = collections.deque()
    is_binary = True

    for i in range(1, V+1):
        if visit[i] != 0:
            continue

        queue.append(i)
        visit[i] = 1
        while queue and is_binary:
            cur = queue.popleft()
            while graph[cur]:
                node = graph[cur].pop()
                queue.append(node)
                if visit[cur] == visit[node]:
                    is_binary = False
                visit[node] = visit[cur]*-1

    print('YES' if is_binary else 'NO')
