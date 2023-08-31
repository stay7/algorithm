"""
2021-07-26
11055.가장 큰 증가 부분 수열
"""


def find_last_element(index: int, num: int):
    max_sum = 0
    for i in range(index, -1, -1):
        if nums[i] < num and max_sum < sums[i]:
            max_sum = sums[i]
    return max_sum


N = int(input())
nums = list(map(int, input().split()))

sums = [0]*len(nums)
for i, num in enumerate(nums):
    sums[i] = num + find_last_element(i, num)
print(max(sums))
