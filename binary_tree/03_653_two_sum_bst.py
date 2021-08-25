# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.traverse(root, set(), k)

    def traverse(self, root, vals, k):
        if not root:
            return False
        if root:
            if k - root.val in vals:
                return True
            vals.add(root.val)
            l = self.traverse(root.left, vals, k)
            r = self.traverse(root.right, vals, k)
            return l or r