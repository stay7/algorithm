"""
2021-04-18
[leetcode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
787. Cheapest Flights Within K Stops
"""

import sys
import collections
from typing import List
import heapq


#
# Runtime ms ()
# Memory MB ()
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        INF = 10001
        d = [INF] * n

        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        d[src] = 0
        queue = [(0, src, 0)]

        while queue:
            price, u, k = heapq.heappop(queue)
            if k <= K:
                k += 1
                for v, w in graph[u]:
                    if d[v] > price + w:
                        d[v] = price + w
                        heapq.heappush(queue, (d[v], v, k))
        if d[dst] == INF:
            return -1
        return d[dst]


if "__main__" == __name__:

    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(Solution().findCheapestPrice(n, edges, src, dst, k))

    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(Solution().findCheapestPrice(n, edges, src, dst, k))

    n = 4
    edges = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
    src = 0
    dst = 3
    k = 1
    print(Solution().findCheapestPrice(n, edges, src, dst, k))

    n = 5
    edges = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    src = 0
    dst = 2
    k = 2
    print(Solution().findCheapestPrice(n, edges, src, dst, k))
