"""
2021-10-08
1043. 거짓말
"""


def find(u):
    if parents[u] == u:
        return u
    parents[u] = find(parents[u])
    return parents[u]


def merge(u, v):
    root_u, root_v = find(u), find(v)
    if root_u == root_v:
        return

    if ranks[root_u] > ranks[root_v]:
        root_u, root_v = root_v, root_u
    parents[root_u] = root_v
    if ranks[root_u] == ranks[root_v]:
        ranks[root_v] += 1


N, M = map(int, input().split())
know_man = list(map(int, input().split()))[1:]
parents = [i for i in range(N + 1)]
ranks = [1] * (N + 1)
for man in know_man:
    merge(0, man)

count = 0
attendance_list = []
for _ in range(M):
    attendance = list(map(int, input().split()))[1:]
    for i in range(1, len(attendance)):
        merge(attendance[0], attendance[i])
    attendance_list.append(attendance)

for attendance in attendance_list:
    is_known = False
    for man in attendance:
        if find(man) == find(0):
            is_known = True
            break
    if not is_known:
        count += 1

print(count)
