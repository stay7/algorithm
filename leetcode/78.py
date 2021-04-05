"""
2021-04-05
[leetcode](https://leetcode.com/problems/subsets/)
78.Subsets
"""

from typing import List


# 약 18분 소요
# Runtime 28 ms (93.47%)
# Memory 14.5 MB (52.09%)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index: int, path: List[int]):
            path = path + [nums[index]]
            out.append(path)
            for i in range(index+1, len(nums)):
                dfs(i, path)
        out = [[]]
        for i in range(len(nums)):
            dfs(i, [])
        return out


if "__main__" == __name__:
    nums = [1, 2, 3]
    nums1 = [0]
    print(Solution().subsets(nums))
    print(Solution().subsets(nums1))
