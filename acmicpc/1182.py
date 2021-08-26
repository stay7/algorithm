"""
2021-08-27
1182. 부분수열의 합
"""

import itertools
N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for k in range(len(nums)):
    for case in list(itertools.combinations(nums, k+1)):
        if sum(case) == S:
            count += 1
print(count)
