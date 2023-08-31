"""
2021-07-25
2442. 별 찍기 - 5
"""

N = int(input())
width = 2*N - 1

for i in range(1, N+1):
    star_num = 2*i - 1
    one_side_white_space_num = (width-star_num)//2
    line = ' '*one_side_white_space_num + '*' * star_num
    print(line)
