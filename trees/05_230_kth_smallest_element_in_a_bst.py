# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        self.k = k
        self.traverse(root)
        return self.res
    def traverse(self, root):
        if root and not self.res:
            self.traverse(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            self.traverse(root.right)
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     self.vals = []
    #     self.traverse(root)
    #     return heapq.nsmallest(k, self.vals)[k-1]
    # def traverse(self, root):
    #     if root:
    #         heapq.heappush(self.vals, root.val)
    #         self.traverse(root.left)
    #         self.traverse(root.right)