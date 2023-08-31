"""
2021-08-04
2004. 조합 0의 개수
"""


def count_divisor(num, divisor):
    count = 0
    while num >= divisor:
        count += num//divisor
        num //= divisor
    return count


N, R = map(int, input().split())
five_count = count_divisor(N, 5) - count_divisor(R, 5) - count_divisor(N-R, 5)
five_count = max(five_count, 0)
two_count = count_divisor(N, 2) - count_divisor(R, 2) - count_divisor(N-R, 2)
two_count = max(two_count, 0)

print(min(five_count, two_count))
