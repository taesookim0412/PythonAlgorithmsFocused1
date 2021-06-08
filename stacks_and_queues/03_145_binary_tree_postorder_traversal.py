# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res
    def traverse(self, root):
        if root:
            self.traverse(root.left)
            self.traverse(root.right)
            self.res.append(root.val)