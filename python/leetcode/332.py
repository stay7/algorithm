"""
2021-04-06
[leetcode](https://leetcode.com/problems/reconstruct-itinerary/)
332. Reconstruct Itinerary
"""
from typing import List
import collections

#
# Runtime ms ()
# Memory MB ()


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(s, graph, visited):
            visited.append(s)
            if len(visited) == len(tickets)+1:
                return visited
            for v in graph[s][::-1]:
                graph[s].remove(v)
                result = dfs(v, graph, visited[:])
                if result:
                    return result
                else:
                    graph[s].append(v)

        graph = collections.defaultdict(list)
        for ticket in tickets:
            a, b = ticket
            graph[a].append(b)
        for v in graph:
            graph[v].sort(reverse=True)

        return dfs("JFK", graph, [])


if "__main__" == __name__:
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets1 = [["JFK", "SFO"], ["JFK", "ATL"], [
        "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    tickets2 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]

    print(Solution().findItinerary(tickets2))
