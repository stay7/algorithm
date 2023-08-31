"""
2021-09-01
2143. 두 배열의 합
"""
import collections
import itertools

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

prefix_a = collections.defaultdict(int)
prefix_b = collections.defaultdict(int)

sum_a = [0]
sum_b = [0]
for i in range(N):
    sum_a.append(sum_a[i] + A[i])
for i in range(M):
    sum_b.append(sum_b[i] + B[i])

cases = itertools.combinations(range(N+1), 2)
for case in cases:
    i, j = case
    prefix_a[sum_a[j]-sum_a[i]] += 1

cases = itertools.combinations(range(M+1), 2)
for case in cases:
    i, j = case
    prefix_b[sum_b[j]-sum_b[i]] += 1

count = 0
for key, value in prefix_a.items():
    if T-key in prefix_b:
        count += value*prefix_b[T-key]
print(count)
