class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: Node):
    def check_height(node: Node):
        if node == None:
            return -1
        left_height = check_height(node.left)
        if left_height == None:
            return None

        right_height = check_height(node.right)
        if right_height == None:
            return None

        if abs(left_height - right_height) > 1:
            return None

        return max(left_height, right_height) + 1

    return check_height(root) != None
