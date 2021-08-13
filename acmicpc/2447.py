"""
2021-08-13
2447. 별 찍기 - 10
"""


def fill(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if i == x+1 and j == y+1:
                continue
            graph[i][j] = '*'


def divide(size, x, y):
    if size == 3:
        return fill(x, y)

    size //= 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            divide(size, x+size*i, y+size*j)


N = int(input())
graph = [[' ' for _ in range(N)] for _ in range(N)]


divide(N, 0, 0)
for i in range(N):
    print(''.join(graph[i]))
