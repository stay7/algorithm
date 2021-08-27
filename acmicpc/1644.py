"""
2021-08-27
1644. 소수의 연속합
"""

N = int(input())
primes = [True for i in range(N+1)]

for i in range(2, N+1):
    if primes[i]:
        for j in range(i+i, N+1, i):
            primes[j] = False
primes = [i for i in range(2, N+1) if primes[i]]
primes.append(0)

low = high = 0
count = partial_sum = 0

while high <= len(primes)-1:
    if partial_sum < N:
        partial_sum += primes[high]
        high += 1
    else:
        partial_sum -= primes[low]
        low += 1

    if partial_sum == N:
        count += 1

print(count)
