"""
2021-08-13
1992. 쿼드트리
"""


def divide(size, x, y):
    if check(size, x, y):
        return graph[x][y]
    size = size//2
    LU = divide(size, x, y)
    LD = divide(size, x+size, y)
    RU = divide(size, x, y+size)
    RD = divide(size, x+size, y+size)
    return '({}{}{}{})'.format(LU, RU, LD, RD)


def check(size, x, y):
    num = graph[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if num != graph[i][j]:
                return False
    return True


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))
print(divide(N, 0, 0))
