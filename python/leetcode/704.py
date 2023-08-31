"""
2021-05-07
[leetcode](https://leetcode.com/problems/binary-search/)
704. Binary Search
"""

from typing import List


# 재귀로 구현한 Binary search
# Runtime 232 ms (78.14%)
# Memory 22.8 MB (28.00%)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(left: int, right: int):
            if left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    return find(mid+1, right)
                if nums[mid] > target:
                    return find(left, mid-1)
            return -1
        index = find(0, len(nums)-1)
        return index if index > -1 else -1


if "__main__" == __name__:
    nums = [2, 5]
    target = 0
    print(Solution().search(nums, target))
