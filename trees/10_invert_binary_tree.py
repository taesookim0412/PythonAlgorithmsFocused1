class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(tree: Node) -> Node:
    if tree is None: return tree
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
    return tree