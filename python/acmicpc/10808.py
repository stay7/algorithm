"""
2021-07-29
10808. 알파벳 개수
"""
import sys

word = sys.stdin.readline().rstrip()
counts = [0 for _ in range(26)]
for char in word:
    index = ord(char) - ord('a')
    counts[index] += 1
for count in counts:
    sys.stdout.write('{} '.format(count))
sys.stdout.write('\n')
