"""
2021-08-08
10815. 숫자 카드
"""


N = int(input())
holds = set(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))
out = []
for card in cards:
    out.append('1' if card in holds else '0')
print(' '.join(out))
