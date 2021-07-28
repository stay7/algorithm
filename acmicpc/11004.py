"""
2021-07-28
11004. K번째 수
"""

N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print(nums[K-1])
