"""
2020-02-13
[leetcode]()
42. Trapping Rain Water
"""


from typing import List


# O(n^2) 으로 풀다가 실패했다.
# 책에 two pointer의 풀이를 보고 작성했다.
# Runtime 52 ms (82.51%)
# Memory 14.9 MB (37.85%)
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        volume = 0

        while left < right:
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                volume += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return volume


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
    height1 = [4, 2, 0, 3, 2, 5]
    print(Solution().trap(height1))
