"""
2021-08-04
1929. 소수 구하기
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


M, N = map(int, input().split())
out = []
for i in range(M, N+1):
    if is_prime(i):
        out.append(i)
for num in out:
    print(num)
