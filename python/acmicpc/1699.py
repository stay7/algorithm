"""
2021-07-27
1699. 제곱수의 합
"""
import math

N = int(input())
nums = [i for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, math.isqrt(i) + 1):
        if nums[i] > nums[i-j*j] + 1:
            nums[i] = nums[i-j*j] + 1
print(nums[-1])
