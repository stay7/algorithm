"""
2021-08-06
9466. 텀 프로젝트
"""
import sys


def dfs(cur):
    index = 0
    stack = [cur]
    path = []
    path_index = {}

    while stack:
        cur = stack.pop()
        if cur in path_index:
            break
        if visit[cur]:
            return 0

        visit[cur] = True
        path.append(cur)
        path_index[cur] = index
        stack.append(choices[cur])
        index += 1

    return index - path_index[cur]


TC = int(sys.stdin.readline())
for _ in range(TC):
    N = int(sys.stdin.readline())
    choices = list(map(int, sys.stdin.readline().split()))
    choices.insert(0, 0)
    visit = [False] * (N+1)
    group_count = 0

    for i in range(1, N+1):
        if not visit[i]:
            group_count += dfs(i)
    sys.stdout.write('{}\n'.format(N-group_count))
