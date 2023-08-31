"""
2021-08-09
10610. 30
"""
import sys

nums = list(map(int, sys.stdin.readline().rstrip()))
nums.sort(reverse=True)
if sum(nums) % 3 == 0 and nums[-1] == 0:
    for num in nums:
        sys.stdout.write('{}'.format(num))
else:
    sys.stdout.write('-1')
sys.stdout.write('\n')
