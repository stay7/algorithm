"""
2021-02-15
[leetcode](https://leetcode.com/problems/array-partition-i/)
561. Array Partition I
"""
from typing import List


# 조금만 생각하면 매우 쉬웠다
# Runtime 248 ms (97.58%)
# Memory 16.9 MB (61.93%)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    print(Solution().arrayPairSum(nums))
