"""
2021-04-15
[leetcode](https://leetcode.com/problems/network-delay-time/)
743. Network Delay Time
"""
from typing import List
import collections
import heapq


# 처음 푸는 다익스트라인데 변형이라 너무 힘들었다...
# Runtime 484 ms (45.66%)
# Memory 16.3 MB (49.57%)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        Q = [(0, k)]
        while Q:
            time, u = heapq.heappop(Q)
            if u not in dist:
                dist[u] = time
                for v, w in graph[u]:
                    heapq.heappush(Q, (time+w, v))

        if len(dist) == n:
            return max(dist.values())
        return -1


if "__main__" == __name__:
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    # print(Solution().networkDelayTime(times, n, k))
    times = [[1, 2, 1]]
    n = 2
    k = 1
    # print(Solution().networkDelayTime(times, n, k))
    times = [[1, 2, 1]]
    n = 2
    k = 2
    # print(Solution().networkDelayTime(times, n, k))
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
    n = 3
    k = 1
    print(Solution().networkDelayTime(times, n, k))
