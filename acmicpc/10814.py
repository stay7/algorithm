"""
2021-07-28
10814. 나이순 정렬
"""

import sys
N = int(sys.stdin.readline())

members = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

members.sort(key=lambda member: member[0])

for member in members:
    age, name = member
    sys.stdout.write('{} {}\n'.format(age, name))
