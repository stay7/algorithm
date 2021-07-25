"""
2021-07-25
2445. 별 찍기 - 8
"""
N = int(input())

width = 2*N
for i in range(1, N):
    star = i
    white_space = width - 2*star
    print('*'*star + ' '*white_space + '*'*star)

print('*'*width)

for i in range(1, N):
    star = N-i
    white_space = width - 2*star
    print('*'*star + ' '*white_space + '*'*star)
