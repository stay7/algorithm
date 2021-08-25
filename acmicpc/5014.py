"""
2021-08-25
5014. 스타트링크
"""

import collections


def bfs(S):
    queue = collections.deque([S, 0])
    height[S] = 0
    while queue:
        cur = queue.popleft()
        count = height[cur]

        if cur == G:
            return height[cur]

        if cur + U <= F and height[cur+U] > count + 1:
            height[cur+U] = count + 1
            queue.append(cur+U)

        if 1 <= cur - D and height[cur-D] > count + 1:
            height[cur-D] = count + 1
            queue.append(cur-D)
    return "use the stairs"


F, S, G, U, D = map(int, input().split())
height = [float('inf')] * (F+1)
print(bfs(S))
