from collections import deque


def route_btw_nodes(G, a, b):
    if a == b:
        return True

    queue = deque()
    visited = set()

    queue.append(a)

    while queue:
        cur = queue.popleft()
        visited[cur] = True
        for node in G[cur]:
            if node not in visited:
                if node == b:
                    return True
                queue.append(node)
    return False
