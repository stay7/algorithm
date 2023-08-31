"""
2021-08-04
6588. 골드바흐의 추측
"""

import sys


nums = []
while True:
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        break
    nums.append(num)

max_num = max(nums)
candidates = [True for _ in range(max_num+1)]
primes = set()
for i in range(2, max_num+1):
    if candidates[i]:
        primes.add(i)
        for j in range(i+i, max_num, i):
            candidates[j] = False

for num in nums:
    for i in range(3, num):
        if i in primes and (num-i) in primes:
            sys.stdout.write('{} = {} + {}\n'.format(num, i, num-i))
            break
