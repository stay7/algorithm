"""
2021-05-07
[leetcode](https://leetcode.com/problems/k-closest-points-to-origin/)
973. K Closest Points to Origin
"""

from typing import List
import heapq


# 무지성 정렬
# Runtime 624 ms (92.61%)
# Memory 19.8 MB (73.10%)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = sorted(points, key=lambda x: x[0]**2+x[1]**2)
        return distances[0:k]


# priority queue를 사용해서 정렬
# Runtime 724 ms (28.93%)
# Memory 20.6 MB (9.30%)
class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, (dist, point[0], point[1]))
        return list(map(lambda node: [node[1], node[2]], heapq.nsmallest(k, heap)))


if "__main__" == __name__:
    points = [[1, 3], [-2, 2]]
    k = 1
    print(Solution1().kClosest(points, k))
