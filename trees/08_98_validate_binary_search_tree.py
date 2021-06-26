# Definition for a binary tree node.
import collections
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    class Solution:
        def isValidBST(self, root: TreeNode) -> bool:
            minVal = -1 * sys.maxsize
            maxVal = sys.maxsize
            treeDeque = collections.deque()
            treeDeque.append([root, minVal, maxVal])
            while treeDeque:
                root, minVal, maxVal = treeDeque.popleft()
                if not root:
                    continue
                if root.val <= minVal or root.val >= maxVal:
                    return False
                treeDeque.append([root.left, minVal, root.val])
                treeDeque.append([root.right, root.val, maxVal])
            return True
    # def isValidBST(self, root: TreeNode) -> bool:
    #     self.res = True
    #     return self.traverse(root)
    #
    # def traverse(self, root, maxVal=sys.maxsize, minVal=-1 * sys.maxsize):
    #     if root and self.res:
    #         if root.val >= maxVal or root.val <= minVal:
    #             return False
    #         return (self.traverse(root.left, root.val, minVal) and
    #                 self.traverse(root.right, maxVal, root.val))
    #     else:
    #         return True
