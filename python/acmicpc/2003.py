"""
2021-08-27
2003. 수들의 합 2
"""

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.append(0)
low, high, section_sum = 0, 0, 0
count = 0

while high <= N:
    if section_sum < M:
        section_sum += nums[high]
        high += 1
    else:
        section_sum -= nums[low]
        low += 1

    if section_sum == M:
        count += 1
print(count)
