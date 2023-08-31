"""
2021-08-18
2579. 계단 오르기
"""
import sys

N = int(sys.stdin.readline().rstrip())
steps = []

for _ in range(N):
    steps.append(int(sys.stdin.readline().rstrip()))

one_steps = []
two_steps = []

for i, step in enumerate(steps):
    if i == 0:
        one_steps.append(steps[0])
        two_steps.append(0)
        continue
    if i == 1:
        one_steps.append(steps[0] + steps[1])
        two_steps.append(steps[1])
        continue

    two_steps.append(max(one_steps[i-2], two_steps[i-2]) + step)
    one_steps.append(two_steps[i-1] + step)

print(max(one_steps[-1], two_steps[-1]))
