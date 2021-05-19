"""
2021-05-19
[leetcode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
167. Two Sum II - Input array is sorted
"""

import collections
from typing import List


# 예전에 풀었던 Two sum문제를 응용해서 푼 문제
# Runtime 60ms (82.04%)
# Memory 15 MB (5.13%)
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = collections.defaultdict(list)
        for i, number in enumerate(numbers):
            nums[number].append(i)
            rest = target-number
            if rest == number and rest in nums:
                if len(nums[rest]) == 1:
                    continue
                return [nums[rest][0] + 1, i + 1]

            if rest in nums:
                return [nums[rest][0]+1, i+1]


# 투 포인터 방식으로 해결 -> 더 깔끔하다
# Runtime 64 ms (58.71%)
# Memory 14.7 MB (58.90%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left+1, right+1]


if "__main__" == __name__:
    numbers = [0, 0, 3, 4]
    target = 0
    print(Solution().twoSum(numbers, target))
