"""
2021-04-30
[leetcode](https://leetcode.com/problems/merge-intervals/)
56.Merge Intervals
"""

from typing import List


# lambda를 사용해서 정렬하는 방법을 알아두면 더 좋을 것 같다
# Runtime 88 ms (46.21%)
# Memory 16.1 MB (83.53%)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        intervals.sort()
        s1, e1 = intervals[0]
        for i in range(1, len(intervals)):
            print(s1, e1)
            s2, e2 = intervals[i]
            if e1 >= s2:
                e1 = max(e1, e2)
            else:
                out.append([s1, e1])
                s1, e1 = s2, e2
        out.append([s1, e1])
        return out


if "__main__" == __name__:
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))

    intervals = [[1, 4], [4, 5]]
    print(Solution().merge(intervals))
