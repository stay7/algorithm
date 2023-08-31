"""
2021-08-18
1744. 수 묶기
"""

import sys

N = int(sys.stdin.readline().rstrip())

pos = []
neg = []
zero_count = one_count = num_sum = 0


for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num < 0:
        neg.append(num)
    elif num > 1:
        pos.append(num)
    elif num == 1:
        one_count += 1
    else:
        zero_count += 1

pos.sort(reverse=True)
neg.sort()

for i in range(0, len(neg), 2):
    if i + 1 < len(neg):
        num_sum += neg[i]*neg[i+1]
    else:
        if zero_count == 0:
            num_sum += neg[i]

for i in range(0, len(pos), 2):
    if i+1 < len(pos):
        num_sum += pos[i]*pos[i+1]
    else:
        num_sum += pos[i]

num_sum += one_count

print(num_sum)
