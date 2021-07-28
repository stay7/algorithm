"""
2021-07-29
9012. 괄호
"""

N = int(input())
for _ in range(N):
    parenthesis = input()
    count = 0
    for char in parenthesis:
        if count < 0:
            break
        if char == '(':
            count += 1
        else:
            count -= 1
    if count == 0:
        print('YES')
    else:
        print('NO')
