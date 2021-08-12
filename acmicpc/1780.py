"""
2021-08-12
11662. 종이의 개수
"""


def check(paper):
    num = paper[0][0]
    for i in range(len(paper)):
        for j in range(len(paper)):
            if num != paper[i][j]:
                return False
    return True


def divide(paper):
    if len(paper) == 1:
        counts[paper[0][0]] += 1
        return
    if check(paper):
        counts[paper[0][0]] += 1
        return

    for i in range(3):
        paper1 = []
        paper2 = []
        paper3 = []
        unit = len(paper)//3
        for row in range(unit*i, unit*(i+1)):
            paper1.append(paper[row][0:unit])
            paper2.append(paper[row][unit:unit*2])
            paper3.append(paper[row][unit*2:])
        divide(paper1)
        divide(paper2)
        divide(paper3)


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

counts = [0, 0, 0]
divide(paper)
print(counts[-1])
print(counts[0])
print(counts[1])
