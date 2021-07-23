"""
2021-07-23
[leetcode](https://leetcode.com/problems/sliding-window-maximum/)
239. Sliding Window Maximum
"""

from collections import deque

#
# Runtime ms ()
# Memory MB ()


class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        window = deque()
        current_max = float('-inf')

        for i, num in enumerate(nums):
            window.append(num)
            if i < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif current_max < num:
                current_max = num
            result.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')
        return result


if "__main__" == __name__:
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))
