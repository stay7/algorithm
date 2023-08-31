"""
2021-07-25
10991. 별 찍기 - 16
"""

N = int(input())
width = 2*N-1

for star in range(1, N+1):
    space = star-1
    blank = N-star
    stars = ' '.join('*'*star)
    print(' '*blank+stars)
