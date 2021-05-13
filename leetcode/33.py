"""
2021-05-13
[leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
33. Search in Rotated Sorted Array
"""

from typing import List


# 문제는 O(log(n))을 요구했지만
# O(n) 연산인데 통과되는 것으로 보아 test case가 부족한 것 같음
# Runtime 44 ms (38.33%)
# Memory 14.4 MB (98.73%)
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


# 책에서는 mid_pivot = (mid+pivot) % len(nums)라는 방법을 사용했는데
# 이해가 힘들어서 왼쪽 배열 오른쪽 배열 중 target이 어디있는지를 찾는 방법으로 품
# Runtime 32 ms (97.31%)
# Memory 14.5 MB (78.93%)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pivot을 찾는 과정
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # pivot을 기준으로 왼쪽 배열, 오른쪽 배열 중 target이 어디에 있는지 찾기
        left, right = 0, len(nums)-1
        if target <= nums[right] and target >= nums[pivot]:
            left = pivot
        else:
            right = pivot - 1

        # target이 있는 배열에서 binary search
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if "__main__" == __name__:
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))
