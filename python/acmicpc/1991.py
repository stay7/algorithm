"""
2021-08-07
1991. 트리 순회
"""

import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(root: Node):
    if not root:
        return
    sys.stdout.write(chr(root.val + ord('A')))
    pre_order(root.left)
    pre_order(root.right)


def in_order(root: Node):
    if not root:
        return

    in_order(root.left)
    sys.stdout.write(chr(root.val + ord('A')))
    in_order(root.right)


def post_order(root: Node):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    sys.stdout.write(chr(root.val + ord('A')))


N = int(sys.stdin.readline().rstrip())
nodes = [Node(i) for i in range(N)]

for _ in range(N):
    cur, left, right = sys.stdin.readline().split()
    cur = ord(cur)-ord('A')
    if left != '.':
        nodes[cur].left = nodes[ord(left) - ord('A')]
    if right != '.':
        nodes[cur].right = nodes[ord(right)-ord('A')]

pre_order(nodes[0])
sys.stdout.write('\n')
in_order(nodes[0])
sys.stdout.write('\n')
post_order(nodes[0])
sys.stdout.write('\n')
