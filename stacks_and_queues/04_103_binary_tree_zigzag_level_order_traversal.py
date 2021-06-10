# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        self.traverse(root)
        for i in range(len(self.res)):
            if (i + 1) & 1 == 0:
                self.res[i] = self.res[i][::-1]
        return self.res

    def traverse(self, root, height=0):
        if root:
            while len(self.res) < height + 1:
                self.res.append([])
            self.res[height].append(root.val)
            self.traverse(root.left, height + 1)
            self.traverse(root.right, height + 1)

    # different kind of zigzag
    # def traverse(self, root, case, height = 0):
    #     if root:
    #         while len(self.res) < height + 1:
    #             self.res.append([])
    #         self.res[height].append(root.val)
    #         if (case & 1 == 0):
    #             self.traverse(root.left, int(case & 1 == 0), height + 1)
    #             self.traverse(root.right, int(case & 1 == 0), height + 1)
    #         else:
    #             self.traverse(root.right, int(case & 1 == 0), height + 1)
    #             self.traverse(root.left, int(case & 1 == 0), height + 1)
