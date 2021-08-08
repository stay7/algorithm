"""
2021-08-08
2110. 공유기 설치
"""

import sys


def set_routers(dist):
    routers = [houses[0]]
    for i in range(1, len(houses)):
        if dist <= houses[i]-routers[-1]:
            routers.append(houses[i])
    return len(routers)


N, C = map(int, sys.stdin.readline().split())
houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline()))
houses.sort()

start, end = 1, houses[-1] - houses[0]
result = end
while start <= end:
    mid = start + (end-start) // 2
    if set_routers(mid) < C:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)
