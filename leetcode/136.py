"""
2021-07-21
[leetcode](https://leetcode.com/problems/single-number/submissions/)
136. Single Number
"""


from typing import List


#
# Runtime 124 ms (94.07%)
# Memory 16.7 MB (59.59%)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
