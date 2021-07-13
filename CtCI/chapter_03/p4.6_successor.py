class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def successor(node: Node):
    if node.right:
        left_most = node.right
        while left_most.left:
            left_most = left_most.left
        return left_most
    ancestor = node.parent
    child = node
    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent
    return ancestor
