"""
2021-07-29
10820. 문자열 분석
"""

while True:
    lower, upper, number, space = 0, 0, 0, 0
    try:
        line = input()
        for char in line:
            if char.isspace():
                space += 1
            elif char.isdecimal():
                number += 1
            elif char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
        print('{} {} {} {}'.format(lower, upper, number, space))
    except EOFError:
        break
