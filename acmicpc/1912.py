"""
2021-08-18
1912. 연속합
"""

N = int(input())
nums = list(map(int, input().split()))
sums = []
sums.append(nums[0])

for i in range(1, len(nums)):
    if sums[i-1] < 0:
        sums.append(nums[i])
    else:
        sums.append(nums[i] + sums[i-1])
print(max(sums))
