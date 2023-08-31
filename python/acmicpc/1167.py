"""
2021-08-07
1167. 트리의 지름
"""

import sys
import collections


def dfs(cur, path):
    max_node, max_path = cur, path
    stack = [(max_node, max_path)]
    visit = set()
    visit.add(max_node)
    while stack:
        cur, path = stack.pop()
        if path > max_path:
            max_node, max_path = cur, path

        for node, dist in graph[cur]:
            if node not in visit:
                stack.append((node, path+dist))
                visit.add(node)
    return max_node, max_path


V = int(sys.stdin.readline().rstrip())
graph = collections.defaultdict(list)
for _ in range(V):
    edges = list(map(int, sys.stdin.readline().split()))
    index = 1
    while edges[index] != -1:
        graph[edges[0]].append((edges[index], edges[index+1]))
        index += 2

max_node, max_path = dfs(1, 0)
max_node, max_path = dfs(max_node, 0)
print(max_path)
