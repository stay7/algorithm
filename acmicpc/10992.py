"""
2021-07-25
10992. 별 찍기 - 17
"""
N = int(input())

if N == 1:
    print('*')
else:
    print(' '*(N-1)+'*')
    for i in range(1, N-1):
        blank = N-i-1
        space = 2*i - 1
        print(' '*blank + '*'+' '*space+'*')
    print('*'*(2*N-1))
