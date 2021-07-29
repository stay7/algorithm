"""
2021-07-29
11656. 접미사 배열
"""

s = input()
out = []
for i in range(len(s)):
    out.append(s[i:])
out.sort()
print('\n'.join(out))
