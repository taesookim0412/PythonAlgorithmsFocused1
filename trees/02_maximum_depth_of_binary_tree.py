#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    height = 0
    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root, 1)
        return self.height
    def traverse(self, root, level):
        if root:
            self.height = max(self.height, level)
            self.traverse(root.left, level + 1)
            self.traverse(root.right, level + 1)