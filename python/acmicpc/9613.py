"""
2021-08-02
9613. GCD 합
"""
import sys


def num_gcd(a, b):
    if b == 0:
        return a
    return num_gcd(b, a % b)


TC = int(sys.stdin.readline())
out = []
for _ in range(TC):
    nums = list(map(int, sys.stdin.readline().split()))
    del nums[0]
    nums.sort(reverse=True)
    sum_gcd = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum_gcd += num_gcd(nums[i], nums[j])
    out.append(str(sum_gcd))


for num in out:
    sys.stdout.write('{}\n'.format(num))
