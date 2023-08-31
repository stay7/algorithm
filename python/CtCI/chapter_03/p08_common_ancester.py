from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def common_ancestor(root: Node, a: Node, b: Node):
    def dfs(node: Node, path: List):
        if node == None:
            return
        path.append(node)
        if node == a or node == b:
            return path

        left_path = dfs(node.left, path)
        if left_path:
            return left_path

        right_path = dfs(node.right, path)
        if right_path:
            return right_path


if __name__ == "__main__":
    a = Node(7)
    b = Node(8)
    graph = Node(1, Node(2, Node(4, Node(6), a), Node(5)), Node(3, b))
    common_ancestor(graph, a, b)
