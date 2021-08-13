"""
2021-08-13
10844. 쉬운 계단 수
"""

N = int(input())
prev = [1]*10

for i in range(2, N+1):
    cur = [prev[1]]
    for j in range(1, 10):
        if j < 9:
            cur.append(prev[j-1]+prev[j+1])
        else:
            cur.append(prev[j-1])
    prev = cur
prev[0] = 0
print(sum(prev) % 1000000000)
