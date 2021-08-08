"""
2021-08-08
10816. 숫자 카드 2
"""
import collections

N = int(input())
holds = collections.Counter(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))

out = []
for card in cards:
    out.append(str(holds[card]))
print(' '.join(out))
