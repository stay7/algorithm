"""
2021-02-16
[leetcode](https://leetcode.com/problems/product-of-array-except-self/)
238. Product of Array Except Self
"""
from typing import List


# 한참동안 고민한 문제
# Runtime 244 ms (61.68%)
# Memory 21.1 MB (64.37%)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        out = []
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)):
            out_index = len(out)-1-i
            out[out_index] *= p
            p *= nums[-i-1]
        return out


if __name__ == "__main__":
    nums = [2, 3, 4, 5]
    print(Solution().productExceptSelf(nums))
