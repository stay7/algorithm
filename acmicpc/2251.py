"""
2021-08-24
2251. 물통
"""
import collections


def bfs():
    queue = collections.deque()
    visit = set()
    queue.append((0, 0, C))
    visit.add((0, 0, C))

    while queue:
        a, b, c = queue.popleft()
        # A -> B
        if a+b > B:
            x, y, z = a+b-B, B, c
        else:
            x, y, z = 0, a+b, c
        if (x, y, z) not in visit:
            queue.append((x, y, z))
            visit.add((x, y, z))

        # B -> A
        if a+b > A:
            x, y, z = A, a+b-A, c
        else:
            x, y, z = a+b, 0, c
        if (x, y, z) not in visit:
            queue.append((x, y, z))
            visit.add((x, y, z))

        # B -> C
        if b+c > C:
            x, y, z = a, b+c-C, C
        else:
            x, y, z = a, 0, b+c
        if (x, y, z) not in visit:
            queue.append((x, y, z))
            visit.add((x, y, z))

        # C -> B
        if b+c > B:
            x, y, z = a, B, b+c-B
        else:
            x, y, z = a, b+c, 0
        if (x, y, z) not in visit:
            queue.append((x, y, z))
            visit.add((x, y, z))

        # C -> A
        if a+c > A:
            x, y, z = A, b, a+c-A
        else:
            x, y, z = a+c, b, 0
        if (x, y, z) not in visit:
            queue.append((x, y, z))
            visit.add((x, y, z))

        # A -> C
        if a+c > C:
            x, y, z = a+c-C, b, C
        else:
            x, y, z = 0, b, a+c
        if (x, y, z) not in visit:
            queue.append((x, y, z))
            visit.add((x, y, z))
    return visit


A, B, C = map(int, input().split())
visit = bfs()
out = set()
for a, b, c in visit:
    if a == 0:
        out.add(c)
out = list(out)
out.sort()
print(' '.join(list(map(str, out))))
