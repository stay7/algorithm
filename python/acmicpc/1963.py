"""
2021-08-20
1963. 소수경로
"""

import sys
import collections


def bfs(src, dest):
    visit = collections.defaultdict(bool)
    queue = collections.deque()
    queue.append((str(src), 0))
    visit[str(src)] = True

    while queue:
        cur, count = queue.popleft()
        for digit in range(4):
            for i in range(10):
                num = cur[:digit] + str(i) + cur[digit+1:]
                if num in primes and visit[num] == False:
                    if num == str(dest):
                        return count+1
                    queue.append((num, count+1))
                    visit[num] = True
    return -1


TC = int(sys.stdin.readline().rstrip())
primes = set([str(i) for i in range(1000, 10000)])

for i in range(2, 10000):
    for prime in range(i*2, 10000, i):
        if str(prime) in primes:
            primes.remove(str(prime))


for _ in range(TC):
    src, dest = map(int, sys.stdin.readline().split())
    if src == dest:
        print(0)
        continue
    count = bfs(src, dest)
    if count == -1:
        print('Impossible')
    else:
        print(count)
