"""
2021-08-31
1561. 놀이 공원
"""

N, M = map(int, input().split())
times = list(map(int, input().split()))

if N <= M:
    print(N)
else:
    left, right = 0, 60000000000
    while left <= right:
        mid = left + (right-left) // 2
        done_count = M
        for i in range(M):
            done_count += mid // times[i]
        if done_count >= N:
            time = mid
            right = mid-1
        else:
            left = mid + 1

    done = M
    for i in range(M):
        done += (time-1) // times[i]
    # print(time, done)

    for i in range(M):
        if time % times[i] == 0:
            done += 1
        if done == N:
            print(i+1)
            break
