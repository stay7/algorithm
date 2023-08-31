"""
2021-04-21
[leetcode](https://leetcode.com/problems/minimum-height-trees/)
310. Minimum Height Trees
"""

import collections
from typing import List


# BFS를 노드마다 수행해서 height를 구하다가 시간초과 발생
# 가장 높이가 낮음 -> edge부터 제거하다보면 남는 노드 (1개 or 2개)가 root
# Runtime 236 ms (67.78%)
# Memory 18.2 MB (86.18%)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = []
        for s in range(n):
            if len(graph[s]) == 1:
                leaves.append(s)
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


if "__main__" == __name__:
    n = 1
    edges = []
    print(Solution().findMinHeightTrees(n, edges))
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(Solution().findMinHeightTrees(n, edges))
    n = 2
    edges = [[0, 1]]
    print(Solution().findMinHeightTrees(n, edges))
