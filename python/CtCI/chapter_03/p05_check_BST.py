class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_BST(root: Node):
    def is_valid(root: Node, min, max):
        if root == None:
            return True

        if min != None and root.val < min:
            return False

        if max != None and root.val >= max:
            return False

        return is_valid(root.left, min, root.val) and is_valid(root.right, root.val, max)

    return is_valid(root, None, None)
