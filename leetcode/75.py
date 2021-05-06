"""
2021-05-06
[leetcode](https://leetcode.com/problems/sort-colors/)
75. Sort Colors
"""


from typing import List


#
# Runtime 28 ms (90.28%)
# Memory 14.2 MB (44.54%)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()


if "__main__" == __name__:
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
