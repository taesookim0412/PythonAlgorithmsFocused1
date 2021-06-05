# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def compare(tree1, tree2):
    return tree1.val == tree2.val

def traverse(tree1, tree2):
    if tree1 and tree2:
        return compare(tree1, tree2) and traverse(tree1.left, tree2.right) and traverse(tree1.right, tree2.left)
    elif tree1 is None and tree2 is None:
        return True
    elif tree1 is None or tree2 is None:
        return False

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return traverse(root.left, root.right)