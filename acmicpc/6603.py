"""
2021-08-27
6603. 로또
"""

import sys
import itertools

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    command = nums[0]
    if command == 0:
        break
    candidates = nums[1:]
    out = list(itertools.combinations(candidates, 6))
    for line in out:
        sys.stdout.write(' '.join(list(map(str, line))))
        sys.stdout.write('\n')
    sys.stdout.write('\n')
