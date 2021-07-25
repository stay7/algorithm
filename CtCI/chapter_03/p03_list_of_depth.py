from collections import defaultdict


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def list_of_depth(node: Node):
    list_dict = defaultdict(list)
    max_depth = 0

    def dfs(node: Node, depth: int):
        if max_depth < depth:
            max_depth = depth
        list_dict[depth].append(node.val)
        if node.left:
            dfs(node.left, depth+1)
        if node.right:
            dfs(node.right, depth+1)

        dfs(node, 0)
