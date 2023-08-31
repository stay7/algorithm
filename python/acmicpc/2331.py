"""
2021-08-06
2331. 반복수열
"""

A, P = map(int, input().split())
nums = [A]
indices = {}
indices[A] = 0

while True:
    last = nums[-1]
    num = 0
    for char in str(last):
        num += int(char) ** P

    if num in indices:
        print(indices[num])
        break
    nums.append(num)
    indices[num] = indices[last] + 1
