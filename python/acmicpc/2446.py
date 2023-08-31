"""
2021-07-25
2446. 별 찍기 - 9
"""
N = int(input())
width = 2*N-1

for star in range(width, 0, -2):
    blank = (width - star) // 2
    print(' '*blank + '*'*star)

for star in range(1, width+1,2):
    if star == 1:
        continue
    blank = (width-star)//2
    print(' '*blank+'*'*star)
