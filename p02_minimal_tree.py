from typing import List


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def minimal_tree(arr: List):
    if len(arr) < 1:
        return None

    center = len(arr)//2
    root = Node(arr[center])

    root.left = minimal_tree(arr[0:center])
    root.right = minimal_tree(arr[center+1:])
    return root


def in_order_traversal(root: Node):
    if root.left:
        in_order_traversal(root.left)
    print(root.val)
    if root.right:
        in_order_traversal(root.right)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    root = minimal_tree(arr)
    in_order_traversal(root)
