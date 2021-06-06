# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    found = False
    targetSum = 0

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.targetSum = targetSum
        self.traverse(root, 0)
        return self.found

    def traverse(self, root, currentSum):
        if root:
            if self.found:
                return
            nodeSum = currentSum + root.val
            if not root.left and not root.right and nodeSum == self.targetSum:
                self.found = True
            else:
                self.traverse(root.left, nodeSum)
                self.traverse(root.right, nodeSum)
