"""
2021-07-28
11652. 카드
"""

import collections
import sys


N = int(sys.stdin.readline())
hash_table = collections.defaultdict(int)

for _ in range(N):
    num = sys.stdin.readline()
    hash_table[num] += 1

counts = []
for key, value in hash_table.items():
    counts.append((int(key), value))

counts.sort(key=lambda x: (x[1], -x[0]))
sys.stdout.write('{}\n'.format(counts[-1][0]))
