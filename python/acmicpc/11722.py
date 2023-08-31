"""
2021-07-26
11722. 가장 긴 감소하는 부분 수열
"""


def find_length(index: int, num: int):
    max_len = 0
    for i in range(index, -1, -1):
        if arr[i] > num and len_list[i] > max_len:
            max_len = len_list[i]
    return max_len


N = int(input())
arr = list(map(int, input().split()))
len_list = [0] * N

for i, num in enumerate(arr):
    len_list[i] = find_length(i, num) + 1
print(max(len_list))
