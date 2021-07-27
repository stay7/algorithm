"""
2021-07-27
9461. 파도반 수열
"""
TC = int(input())
for _ in range(TC):
    N = int(input())
    nums = [0, 1, 1, 1, 2, 2, ]
    for i in range(6, N+1):
        nums.append(nums[i-1] + nums[i-5])
    print(nums[N])
