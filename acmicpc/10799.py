"""
2021-07-29
10799. 쇠막대기
"""

sticks = input()
sticks = sticks.replace('()', 'l')
count = 0
on_progress = 0

for i, char in enumerate(sticks):
    if char == '(':
        on_progress += 1
        count += 1
    elif char == ')':
        on_progress -= 1
    else:
        count += on_progress

print(count)
