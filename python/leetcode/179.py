"""
2021-05-04
[leetcode](https://leetcode.com/problems/largest-number/submissions/)
179. Largest Number
"""

from typing import List


# 유연한 사고... 정렬을 할 떄 하나의 키가 아닌 두 개를 더하거나 뺴거나도 생각하자
# Runtime 60 ms (20.97%)
# Memory 14.3 MB (29.29%)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(lambda x: str(x), nums))
        for i in range(0, len(nums)-1):
            for j in range(i, len(nums)):
                num_ij = nums[i] + nums[j]
                num_ji = nums[j] + nums[i]
                if num_ij < num_ji:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int(''.join(nums)))


if "__main__" == __name__:
    nums = [10, 2]
    print(Solution().largestNumber(nums))
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))
