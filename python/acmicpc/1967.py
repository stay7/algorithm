"""
2021-08-07
1967. 트리의 지름
"""

import collections


def dfs(cur, weight):
    stack = [(cur, weight)]
    max_node, max_weight = cur, weight
    visit = set()
    visit.add(cur)

    while stack:
        cur, cur_weight = stack.pop()
        if cur_weight > max_weight:
            max_node, max_weight = cur, cur_weight
        for node, weight in graph[cur]:
            if node not in visit:
                stack.append((node, cur_weight + weight))
                visit.add(node)
    return max_node, max_weight


N = int(input())
graph = collections.defaultdict(list)

for _ in range(N-1):
    node, child, weight = map(int, input().split())
    graph[node].append((child, weight))
    graph[child].append((node, weight))

node, weight = dfs(1, 0)
node, weight = dfs(node, 0)
print(weight)
