"""
2021-07-29
11655. ROT13
"""

s = input()
out = []
ord_a,  ord_A = ord('a'), ord('A')

for char in s:
    if char.islower():
        num = ord_a + (ord(char)-ord_a+13) % 26
        out.append(chr(num))
    elif char.isupper():
        num = ord_A + (ord(char) - ord_A + 13) % 26
        out.append(chr(num))
    else:
        out.append(char)
print(''.join(out))
