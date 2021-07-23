"""
2021-07-23
10950. A+B - 3
"""


def solution():
    for _ in range(int(input())):
        A, B = map(int, input().split())
        print(A+B)


if "__main__" == __name__:
    solution()
