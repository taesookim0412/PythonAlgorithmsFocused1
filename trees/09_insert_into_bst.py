class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#without duplicates
def insert_into_bst(bst: Node, val: int) -> Node:
    res = traverse_bst(bst, val, bst)
    if res[3] is True:
        return bst
    node, left, right, invalid = res
    if left:
        node.left = Node(val)
    elif right:
        node.right = Node(val)
    elif not left and not right:
        return node
    return bst

#returns [node, left, right, invalid]
def traverse_bst(curr, val, root, invalid=False):
    if curr is None:
        return [Node(val), False, False, invalid]
    if curr.val == val:
        return [None, None, None, True]
    if val < curr.val:
        if curr.left is None:
            return [curr, True, False, invalid]
        return traverse_bst(curr.left, val, root)
    if val > curr.val:
        if curr.right is None:
            return [curr, False, True, invalid]
        return traverse_bst(curr.right, val, root)
    return root


#with duplicates
# def insert_bst(bst: Node, val: int) -> Node:
#     return traverse_bst(bst, val, bst)
# def traverse_bst(curr, val, root):
#     if curr is None:
#         return Node(val)
#     if val <= curr.val:
#         if curr.left is None:
#             curr.left = Node(val)
#             return root
#         return traverse_bst(curr.left, val, root)
#     if val > curr.val:
#         if curr.right is None:
#             curr.right = Node(val)
#             return root
#         return traverse_bst(curr.right, val, root)
#     return root
