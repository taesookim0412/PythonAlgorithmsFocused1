# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverse(self, root, level=0):
        if root:
            if len(self.res) < level + 1:
                while len(self.res) < level + 1:
                    self.res.append([])
            self.res[level].append(root.val)
            self.traverse(root.left, level + 1)
            self.traverse(root.right, level + 1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        self.traverse(root)
        return self.res