"""
2021-08-08
2805. 나무 자르기
"""

import collections


def sum_cut(num):
    sum = 0
    for tree, count in trees.items():
        if tree > num:
            sum += (tree-num)*count
    return sum


N, M = map(int, input().split())
trees = collections.Counter(map(int, input().split()))

left, right = 0, max(trees)
result = 0

while left <= right:
    mid = left + (right-left) // 2
    if sum_cut(mid) < M:
        right = mid - 1
    else:
        left = mid + 1
        result = mid
print(result)
