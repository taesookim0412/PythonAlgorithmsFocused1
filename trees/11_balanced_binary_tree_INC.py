class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#incorrect
def is_balanced(tree: Node) -> bool:
    res = traverse(tree)
    res.sort()
    print(res)
    for i in range(1, len(res)):
        if res[i] - res[i-1] > 1:
            return False
    return True

def traverse(curr, height = 1, heights = [], isRoot=True):
    if curr is None:
        heights.append(height)
        return None
    traverse(curr.left, height + 1, heights, False)
    traverse(curr.right, height + 1, heights, False)
    if isRoot:
        return heights
    return None