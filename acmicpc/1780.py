"""
2021-08-12
11662. 종이의 개수
"""


def check(size, x, y):
    num = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if num != paper[i][j]:
                return False
    return True


def divide(size, x, y):
    if size == 1:
        counts[paper[x][y]] += 1
        return
    if check(size, x, y):
        counts[paper[x][y]] += 1
        return

    size //= 3
    divide(size, x, y)
    divide(size, x, y+size)
    divide(size, x, y+size*2)
    divide(size, x+size, y)
    divide(size, x+size, y+size)
    divide(size, x+size, y+size*2)
    divide(size, x+size*2, y)
    divide(size, x+size*2, y+size)
    divide(size, x+size*2, y+size*2)


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

counts = [0, 0, 0]
divide(len(paper), 0, 0)
print(counts[-1])
print(counts[0])
print(counts[1])
