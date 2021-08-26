"""
2021-08-25
1759. 암호 만들기
"""

import itertools

L, C = map(int, input().split())
chars = input().split()
chars.sort()

vowers = set()
consonants = list()

dictionary = {}

for i, char in enumerate(chars):
    dictionary[char] = i
    if char in set(['a', 'e', 'i', 'o', 'u']):
        vowers.add(char)
    else:
        consonants.append(char)

out = set()
for i in range(1, min(L-1, len(vowers)+1)):
    vower = list(itertools.combinations(vowers, i))
    consonant = list(itertools.combinations(consonants, L-i))
    for v in vower:
        for c in consonant:
            candidate = list(v+c)
            candidate.sort()
            out.add(''.join(candidate))
out = list(out)
out.sort()
print('\n'.join(out))
