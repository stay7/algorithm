"""
2021-08-21
11403. 경로 찾기
"""
import sys
N = int(sys.stdin.readline().rstrip())

graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == '1' and graph[k][j] == '1':
                graph[i][j] = '1'


for line in graph:
    print(' '.join(line))
