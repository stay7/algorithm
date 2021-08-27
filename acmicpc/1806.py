"""
2021-08-27
1806. 부분합
"""

N, S = map(int, input().split())
nums = list(map(int, input().split()))
nums.append(0)
out = []

partial_sum = 0
low = high = 0
minimum = len(nums)

while high <= N:
    if partial_sum >= S:
        partial_sum -= nums[low]
        low += 1
    else:
        partial_sum += nums[high]
        high += 1
    if partial_sum >= S and high-low < minimum:
        minimum = high-low

if minimum == len(nums):
    minimum = 0
print(minimum)
