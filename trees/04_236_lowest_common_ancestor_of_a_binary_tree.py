class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = None
        self.traverse(root, p, q)
        return self.answer
    def traverse(self, root, p, q):
        if root:
            left = self.traverse(root.left, p, q)
            right = self.traverse(root.right, p, q)
            mid = root == p or root == q
            if left + right + mid >= 2:
                self.answer = root
            return left or right or mid
        return False