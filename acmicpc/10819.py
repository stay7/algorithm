"""
2021-08-19
10819. 차이를 최대로
"""

from itertools import permutations


def calc(nums):
    out = 0
    for i in range(len(nums)-1):
        out += abs(nums[i] - nums[i+1])
    return out


input()
nums = list(map(int, input().split()))
cases = list(permutations(nums))
cur_max = float('-inf')
for case in cases:
    result = calc(case)
    if result > cur_max:
        cur_max = result

print(cur_max)
