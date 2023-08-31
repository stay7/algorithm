"""
2021-08-19
1107. 리모컨
"""


def sol():
    N = int(input())
    M = int(input())
    broken = set()
    if M > 0:
        broken = set(input().split())
    count = 0
    increase = decrease = N
    out = abs(N-100)

    while len(set(str(increase)).intersection(broken)) > 0 and len(set(str(decrease)).intersection(broken)) > 0:
        if increase == 100 or decrease == 100:
            return count
        increase += 1
        decrease -= 1
        count += 1

    if len(set(str(increase)).intersection(broken)) == 0:
        out = min(out, count+len(str(increase)))
    if len(set(str(decrease)).intersection(broken)) == 0:
        out = min(out, count + len(str(decrease)))
    return out


print(sol())
