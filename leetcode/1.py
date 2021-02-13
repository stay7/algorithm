"""
2020-02-13
[leetcode](https://leetcode.com/problems/two-sum/)
1. Two Sum
"""

from typing import List


# 이전에 풀어본 문제
# Runtime 56 ms (22.98%)
# Memory 14.5 MB (47.22%)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            find = target - num
            if find in dict:
                return [i, dict[find]]
            dict[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
