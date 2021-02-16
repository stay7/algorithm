"""
2020-02-14
[leetcode](https://leetcode.com/problems/two-sum/)
15. 3Sum
"""
from typing import List


# 몹시 어려웠다..
# 지금까지 푼 문제 중 시간도 가장 오래 걸린 문제
# Runtime 788 ms (82.82%)
# Memory 17.5 MB (52.04%)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                sum = num + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    while left + 1 < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right - 1 and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


if "__main__" == __name__:
    nums = [-1, 0, 1, 2, -1, -4, -1, 1]
    print(Solution().threeSum(nums))
