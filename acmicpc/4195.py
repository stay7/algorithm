"""
2021-09-05
4195. 친구 네트워크
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
        return counts[u]

    if rank[u] > rank[v]:
        u, v = v, u
    parents[u] = v
    counts[v] += counts[u]
    if rank[u] == rank[v]:
        rank[v] += 1
    return counts[v]


TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    parents = {}
    rank = {}
    counts = {}

    for _ in range(int(sys.stdin.readline().rstrip())):
        A, B = sys.stdin.readline().split()
        if not A in parents:
            parents[A] = A
            rank[A] = 1
            counts[A] = 1
        if not B in parents:
            parents[B] = B
            rank[B] = 1
            counts[B] = 1

        print(merge(A, B))
