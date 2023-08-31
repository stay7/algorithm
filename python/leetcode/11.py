"""
2021-
[leetcode](https://leetcode.com/problems/container-with-most-water/)
11. Container With Most Water
"""

#
# Runtime 1007 ms (10.48%)
# Memory 27.5 MB (75.54%)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_vol = 0

        while left <= right:
            vol = (right-left)*min(height[left], height[right])
            if vol > max_vol:
                max_vol = vol

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_vol


if "__main__" == __name__:
    Solution()
