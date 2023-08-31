"""
2021-07-25
11021.A+B - 7
"""
TC = int(input())

for i in range(TC):
    A, B = map(int, input().split())
    print('Case #{}: {}'.format(i+1, A+B))
