"""
2021-08-06
2677. 단지번호붙이기
"""
import sys
import collections


def bfs(i, j):
    count = 0
    queue = collections.deque()
    queue.append((i, j))
    graph[i][j] = '0'
    while queue:
        cur_i, cur_j = queue.popleft()
        count += 1
        # Up
        if cur_i > 0 and graph[cur_i-1][cur_j] == '1':
            queue.append((cur_i-1, cur_j))
            graph[cur_i-1][cur_j] = '0'
        # Down
        if cur_i < len(graph)-1 and graph[cur_i+1][cur_j] == '1':
            queue.append((cur_i+1, cur_j))
            graph[cur_i+1][cur_j] = '0'
        # Left
        if cur_j > 0 and graph[cur_i][cur_j-1] == '1':
            queue.append((cur_i, cur_j-1))
            graph[cur_i][cur_j-1] = '0'
        # Right
        if cur_j < len(graph)-1 and graph[cur_i][cur_j+1] == '1':
            queue.append((cur_i, cur_j+1))
            graph[cur_i][cur_j+1] = '0'
    return count


N = int(input())
graph = []
complex = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            complex.append(bfs(i, j))
complex.sort()
sys.stdout.write('{}\n'.format(len(complex)))
for num in complex:
    sys.stdout.write('{}\n'.format(num))
