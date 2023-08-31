"""
2021-05-13
[leetcode](https://leetcode.com/problems/intersection-of-two-arrays/)
349. Intersection of Two Arrays
"""

from typing import List


# set의 intersection 함수를 이용해 풀어본 풀이
# Runtime 48 ms (46.06%)
# Memory 14.4 MB (44.35%)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)
        return nums1 & nums2


if "__main__" == __name__:
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersection(nums1, nums2))
