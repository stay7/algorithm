"""
2021-08-23
9019. DSLR
"""

import sys
import collections


def command_L(num):
    return (num % 1000)*10 + (num//1000)


def command_R(num):
    return (num % 10) * 1000 + num // 10


def command_S(num):
    return (num + 9999) % 10000


def command_D(num):
    return (num*2) % 10000


def bfs(start, end):
    queue = collections.deque()
    queue.append(start)
    cmd[start] = '0'
    while queue:
        cur = queue.popleft()

        D = command_D(cur)
        if cmd[D] == '':
            queue.append(D)
            cmd[D] = 'D'
            src[D] = cur
            if D == end:
                break

        S = command_S(cur)
        if cmd[S] == '':
            queue.append(S)
            cmd[S] = 'S'
            src[S] = cur
            if S == end:
                break

        L = command_L(cur)
        if cmd[L] == '':
            queue.append(L)
            cmd[L] = 'L'
            src[L] = cur
            if L == end:
                break

        R = command_R(cur)
        if cmd[R] == '':
            queue.append(R)
            cmd[R] = 'R'
            src[R] = cur
            if R == end:
                break


TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    A, B = map(int, sys.stdin.readline().split())
    cmd = ['' for _ in range(10000)]
    src = ['' for _ in range(10000)]
    bfs(A, B)
    out = []
    while B != A:
        out.append(cmd[B])
        B = src[B]
    out.reverse()
    sys.stdout.write('{}\n'.format(''.join(out)))
