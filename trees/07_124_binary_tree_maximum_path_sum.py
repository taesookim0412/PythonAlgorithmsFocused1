# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -1 * sys.maxsize
        self.traverse(root)
        return self.maxSum
    def traverse(self, root):
        if root:
            l = max(0, self.traverse(root.left))
            r = max(0, self.traverse(root.right))
            total = l + r + root.val
            self.maxSum = max(self.maxSum, total)
            return max(l + root.val, r + root.val)
        else:
            return 0