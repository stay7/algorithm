"""
2021-
[leetcode](https://leetcode.com/problems/longest-consecutive-sequence/)
128. Longest Consecutive Sequence
"""

from typing import List


#
# Runtime ms ()
# Memory MB ()
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_longest = 0

        for num in nums:
            cur_num = num
            cur_longest = 1
            if num - 1 not in num_set:
                while cur_num + 1 in num_set:
                    cur_longest += 1
                    cur_num += 1
                max_longest = max(max_longest, cur_longest)
        return max_longest


if "__main__" == __name__:
    Solution()
