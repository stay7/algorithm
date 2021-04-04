"""
2021-04-04
[leetcode](https://leetcode.com/problems/combinations/)
77. Combinations
"""

from typing import List


#
# Runtime 564 ms (28.31%)
# Memory 15.9 MB (14.43%)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combination(elements: List[int], chosen: List[int]):
            if len(chosen) == k:
                result.append(chosen)
                return

            new_elements = elements.copy()
            for element in elements:
                new_chosen = chosen.copy()
                new_chosen.append(element)
                new_elements.remove(element)
                combination(new_elements, new_chosen)

        result = []
        combination(list(range(1, n+1)), [])
        return result


if "__main__" == __name__:
    print(Solution().combine(4, 2))
    print(Solution().combine(1, 1))
