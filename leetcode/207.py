"""
2021-04-08
[leetcode](https://leetcode.com/problems/course-schedule/)
207. Course Schedule
"""

from typing import List
import collections


# 처음에 running과 done을 list로 구현
# Runtime 168 ms (10.57%)
# Memory 17.6 MB (16.91%)

# running과 done을 set으로 구현 차이가 엄청 크다
# Runtime 92 ms (89.32%)
# Memory 17.4 MB (24.01%)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(s: int):
            if s in running:
                return False
            running.append(s)

            for v in graph[s]:
                if not v in done:
                    result = dfs(v)
                    if result == False:
                        return False
            running.remove(s)
            done.append(s)

        running = set()
        done = set()
        graph = collections.defaultdict(list)

        for prerequisite in prerequisites:
            a, b = prerequisite
            graph[a].append(b)

        for i in range(numCourses):
            result = dfs(i)
            if result == False:
                return False
        return True


if "__main__" == __name__:
    # numCourses = 2
    # prerequisites = [[1, 0]]
    # print(Solution().canFinish(numCourses, prerequisites))
    # numCourses = 2
    # prerequisites = [[1, 0], [0, 1]]
    # print(Solution().canFinish(numCourses, prerequisites))
    numCourses = 4
    prerequisites = [[1, 3], [2, 0], [2, 3]]
    print(Solution().canFinish(numCourses, prerequisites))
