"""
2021-08-26
1717. 집합의 표현
"""

import sys


def find(u):
    if parents[u] == u:
        return u
    parents[u] = find(parents[u])
    return parents[u]


def merge(u, v):
    u, v = find(u), find(v)
    if u == v:
        return

    # u의 높이가 더 높으면 u와 v를 swap
    # 높이가 낮은 트리를 높은 트리의 루트에 붙임 -> 이렇게 하지 않으면 linked list처럼 한 줄이 될 수 있음
    if rank[u] > rank[v]:
        u, v = v, u

    # u의 부모를 v에 붙인다
    parents[u] = v

    # u와 v의 높이가 다르면 merge해도 높이 변화 없지만
    # u와 v의 높이가 같으면 높이가 1 증가
    if rank[u] == rank[v]:
        rank[v] += 1


N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N + 1)]
rank = [1] * (N + 1)

for _ in range(M):
    op, u, v = map(int, sys.stdin.readline().split())
    if op == 0:
        merge(u, v)
    else:
        if find(u) == find(v):
            print("YES")
        else:
            print("NO")
