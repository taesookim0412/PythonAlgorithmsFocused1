#662. Maximum Width of Binary Tree
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelOrder = []
        q = collections.deque([(root, 1)])
        width = 0
        #at a level
        while q:
            left, right = sys.maxsize, -1 * sys.maxsize
            for i in range(len(q)):
                curr, height = q.popleft()
                #TODO: pass width instead of height

            width = max(width, right - left + 1)
        return width
#tle
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         levelOrder = []
#         q = collections.deque([root])
#         width = 0
#         #at a level
#         while q:
#             level_q = collections.deque()
#             left, right = sys.maxsize, -1 * sys.maxsize
#             found = False
#             for i in range(len(q)):
#                 curr = q.popleft()
#                 if curr is None:
#                     level_q.append(None)
#                     q.append(None)
#                     q.append(None)
#                 else:
#                     found = True
#                     left = min(left, i)
#                     right = max(right, i)
#                     level_q.append(curr.val)
#                     q.append(curr.left)
#                     q.append(curr.right)
#             if not found:
#                 break
#             width = max(width, right - left + 1)
#             levelOrder.append(level_q)
#         return width
#TLE
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelOrder = []
        q = collections.deque([root])
        width = 0
        while q:
            level_q = collections.deque()
            found = False
            for i in range(len(q)):
                curr = q.popleft()
                if curr is None:
                    level_q.append(None)
                    q.append(None)
                    q.append(None)
                else:
                    found = True
                    level_q.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if not found:
                break
            levelOrder.append(level_q)
        for height in levelOrder:
            left, right = sys.maxsize, -1 * sys.maxsize
            for i in range(len(height)):
                if height[i]:
                    left = min(left, i)
                    right = max(right, i)
            if left != sys.maxsize:
                width = max(width, right - left + 1)
        return width