"""
2021-08-09
2875. 대회 or 인턴
"""
import math
N, M, K = map(int, input().split())

team_num = min(N//2, M)
member_num = team_num*3
rest = N+M - member_num
if rest > K:
    print(team_num)
else:
    needs = K-rest
    team_num -= math.ceil(needs/3)
    print(max(0, team_num))
