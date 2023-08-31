"""
2021-07-26
9465. 스티커
"""
import sys

TC = int(input())
while TC:
    TC -= 1
    row_len = int(input())
    stickers = []
    for _ in range(2):
        row = [0, 0]
        row = row + list(map(int, input().split()))
        stickers.append(row)
    for j in range(2, len(stickers[1])):
        stickers[0][j] += max(stickers[1][j-1], stickers[1][j-2])
        stickers[1][j] += max(stickers[0][j-1], stickers[0][j-2])
    print(max(stickers[0][row_len+1], stickers[1][row_len+1]))
