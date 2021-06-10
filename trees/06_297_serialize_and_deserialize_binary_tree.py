# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.serializedBst = []
        self.serialize_traverse(root)
        return self.serializedBst

    def serialize_traverse(self, root):
        if root:
            self.serializedBst.append(root.val)
            self.serialize_traverse(root.left)
            self.serialize_traverse(root.right)
        else:
            self.serializedBst.append(None)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.deserialize_traverse(iter(data))

    def deserialize_traverse(self, data):
        val = next(data)
        if val is None:
            return None
        root = TreeNode(val)
        root.left = self.deserialize_traverse(data)
        root.right = self.deserialize_traverse(data)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))