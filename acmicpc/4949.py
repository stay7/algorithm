"""
2021-10-08
4949. 균형잡힌 세상
"""
import sys


def check(line: str):
    open = [
        "(",
        "[",
    ]
    close = [")", "]"]

    stack = []
    for char in line:
        if char in open:
            stack.append(char)
        if char in close:
            if not stack:
                return False
            last_bracket = stack.pop()
            if char == close[0]:
                if last_bracket != open[0]:
                    return False
            else:
                if last_bracket != open[1]:
                    return False
    return len(stack) == 0


while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break
    if check(line):
        print("yes")
    else:
        print("no")
