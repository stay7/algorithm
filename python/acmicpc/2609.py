"""
2021-07-31
2609. 최대공약수와 최소공배수
"""

# math 라이브러리
import math

A, B = map(int, input().split())
print(math.gcd(A, B))
print(math.lcm(A, B))


# 유클리드 호제법
def sol():
    def gcd(A, B):
        if B == 0:
            return A
        return gcd(B, A % B)

    A, B = map(int, input().split())
    if A < B:
        A, B = B, A
    divistor = gcd(A, B)
    print(divistor)
    print(int(A*B/divistor))
