"""
2021-08-20
1697. 숨바꼭질
"""

import collections

N, K = map(int, input().split())


def bfs(N, K):
    queue = collections.deque()
    queue.append((N, 0))
    MAX = 100001
    visits = [False for i in range(MAX)]
    while queue:
        cur, count = queue.popleft()
        if cur == K:
            return count

        if cur+1 < MAX and not visits[cur+1]:
            queue.append((cur+1, count+1))
            visits[cur+1] = True
        if cur-1 >= 0 and not visits[cur-1]:
            queue.append((cur-1, count+1))
            visits[cur-1] = True
        if cur*2 < MAX and not visits[cur*2]:
            queue.append((cur*2, count+1))
            visits[cur*2] = True


print(bfs(N, K))
