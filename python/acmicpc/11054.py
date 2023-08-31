"""
2021-07-26
11054. 가장 긴 감소하는 부분 수열
"""


def find_increase(index: int, num: int):
    result = 0
    for i in range(index, -1, -1):
        if arr[i] < num and result < increase_len[i]:
            result = increase_len[i]
    return result


def find_decrease(index: int, num: int):
    result = 0
    for i in range(index+1, N):
        if arr[i] < num and result < decrease_len[i]:
            result = decrease_len[i]
    return result


N = int(input())
arr = list(map(int, input().split()))
decrease_len = [0]*N
increase_len = [0]*N
sum_len = 0

for i in range(N-1, -1, -1):
    decrease_len[i] = find_decrease(i, arr[i]) + 1

for i, num in enumerate(arr):
    increase_len[i] = find_increase(i, num) + 1
    if sum_len < decrease_len[i] + increase_len[i]:
        sum_len = decrease_len[i] + increase_len[i]
print(sum_len-1)
