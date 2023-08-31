"""
2021-04-28
[leetcode](https://leetcode.com/problems/kth-largest-element-in-an-array/)
215. Kth Largest Element in an Array
"""

import heapq
from typing import List


# 정렬을 이용한 경우
# Runtime 60 ms (86.47%)
# Memory 15.1 MB (43.11%)
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


# heapq의 nlargest를 사용한 경우
# Runtime 60 ms (86.47%)
# Memory 15 MB (74.52%)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if "__main__" == __name__:
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))
