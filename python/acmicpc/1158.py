"""
2021-07-29
1158. 요세푸스 문제
"""

import sys
import collections


N, K = map(int, sys.stdin.readline().rstrip().split())
out = []
queue = collections.deque()
for i in range(N):
    queue.append(str(i+1))


step = 0
while queue:
    step += 1
    num = queue.popleft()
    if step == K:
        out.append(num)
        step = 0
    else:
        queue.append(num)


sys.stdout.write('<{}>\n'.format(', '.join(out)))
