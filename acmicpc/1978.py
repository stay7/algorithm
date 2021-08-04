"""
2021-08-04
1978. 소수 찾기
"""


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if i*i > num:
            return True
        if num % i == 0:
            return False
    return True


N = int(input())
prime_count = 0
nums = map(int, input().split())


for num in nums:
    if is_prime(num):
        prime_count += 1
print(prime_count)
