"""
2021-07-25
2522. 별 찍기 - 12
"""

N = int(input())
for i in range(1, N):
    print(' '*(N-i)+'*'*i)
print('*'*N)
for i in range(1, N):
    print(' '*i+'*'*(N-i))
