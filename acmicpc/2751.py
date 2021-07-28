"""
2021-07-28
2751. 수 정렬하기 2
"""
import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
for i in range(N):
    sys.stdout.write('{}\n'.format(nums[i]))
