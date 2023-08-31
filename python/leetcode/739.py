"""
2021-02-27
[leetcode](https://leetcode.com/problems/daily-temperatures/)
739. Daily Temperatures
"""

from typing import List


# Runtime 484 ms(96.65%)
# Memory 19MB (30.84%)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        out = [0] * len(T)
        stack = []

        for i, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                j = stack.pop()
                out[j] = i-j
            stack.append(i)
        return out


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(T))
