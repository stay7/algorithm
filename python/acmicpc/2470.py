"""
2021-08-31
2740. 두 용액
"""


N = int(input())
nums = list(map(int, input().split()))
nums.sort()

left = 0
right = len(nums) - 1
cur_min, cur_pos = nums[right] + nums[left], (left, right)

while left < right:
    diff = nums[left] + nums[right]
    if abs(diff) < abs(cur_min):
        cur_min = diff
        cur_pos = (left, right)

    if diff > 0:
        right -= 1
    elif diff < 0:
        left += 1
    else:
        break

left, right = cur_pos
print(nums[left], nums[right])
