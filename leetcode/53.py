"""
2021-
[leetcode](https://leetcode.com/problems/maximum-subarray/)
53. Maximum Subarray
"""

from typing import List

#
# Runtime ms ()
# Memory MB ()
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)


# 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum


if "__main__" == __name__:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
