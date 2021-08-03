"""
2021-08-03
2089. -2진수
"""

N = int(input())
base = -2
out = []
if N == 0:
    out.append('0')

while N != 0:
    remainer = N % -2
    N = N//-2
    if remainer == -1:
        N += 1
        remainer = 1
    out.append(str(remainer))
print(''.join(out)[::-1])
