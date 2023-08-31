"""
2021-08-03
2745. 진법 변환
"""

digits, B = input().split()
num = 0
exp = len(digits) - 1
for char in digits:
    if ord(char) > ord('9'):
        out = 10 + ord(char) - ord('A')
    else:
        out = int(char)
    num += out * (int(B)**exp)
    exp -= 1
print(num)
