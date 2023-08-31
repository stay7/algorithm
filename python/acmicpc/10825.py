"""
2021-07-28
10825.국영수
"""

import sys
from functools import cmp_to_key


def compare(a, b):
    if a[1] == b[1]:
        if a[2] == b[2]:
            if a[3] == b[3]:
                if a[0] == b[0]:
                    return 0
                return 1 if a[0] > b[0] else -1
            return b[3] - a[3]
        return a[2] - b[2]
    return b[1] - a[1]


N = int(input())

students = []
for _ in range(N):
    name, korean, math, english = sys.stdin.readline().split()
    students.append((name, int(korean), int(math), int(english)))

students.sort(
    key=lambda student: (-student[1], student[2], -student[3], student[0]))
# students.sort(key=cmp_to_key(compare))

for student in students:
    sys.stdout.write('{}\n'.format(student[0]))
