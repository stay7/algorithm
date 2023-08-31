"""
2021-07-27
2225. 합분해
"""


def sol():
    N, K = map(int, input().split())
    if K == 1:
        return 1
    nums = [1] * (N+1)
    for _ in range(2, K):
        for i in range(1, N+1):
            nums[i] = nums[i-1] + nums[i]
    return sum(nums) % 1000000000


print(sol())
