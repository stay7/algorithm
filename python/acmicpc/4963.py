"""
2021-08-07
4963. 섬의 개수
"""


def dfs(i, j):
    def addRoute(pos):
        stack.append(pos)
        graph[pos[0]][pos[1]] = '0'

    stack = [(i, j)]
    graph[i][j] = '0'

    while stack:
        i, j = stack.pop()
        if i > 0:
            # Up
            if graph[i-1][j] == '1':
                addRoute((i-1, j))
            # Up Left
            if j > 0 and graph[i-1][j-1] == '1':
                addRoute((i-1, j-1))
            # Up Right
            if j < w - 1 and graph[i-1][j+1] == '1':
                addRoute((i-1, j+1))

        if i < h-1:
            # Down
            if graph[i+1][j] == '1':
                addRoute((i+1, j))
            # Down Left
            if j > 0 and graph[i+1][j-1] == '1':
                addRoute((i+1, j-1))
            # Down Right
            if j < w - 1 and graph[i+1][j+1] == '1':
                addRoute((i+1, j+1))
        # Left
        if j > 0 and graph[i][j-1] == '1':
            addRoute((i, j-1))
        if j < w - 1 and graph[i][j+1] == '1':
            addRoute((i, j+1))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(input().split()))

    island_count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '1':
                dfs(i, j)
                island_count += 1
    print(island_count)
