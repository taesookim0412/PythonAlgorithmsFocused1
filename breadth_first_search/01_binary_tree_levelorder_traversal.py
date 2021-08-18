import collections
from typing import List


def level_order_traversal(root: Node) -> List[List[int]]:
    res = []
    q = collections.deque([[root, 1]])
    while len(q):
        curr, height = q.popleft()
        if curr is None:
            continue
        while len(res) < height:
            res.append([])
        res[height - 1].append(curr.val)
        if curr.right:
            q.appendleft([curr.right, height + 1])
        if curr.left:
            q.appendleft([curr.left, height + 1])
    return res



# this is dfs
# def level_order_traversal(root: Node) -> List[List[int]]:
#     res = []
#     traverse(root, res)
#     return res
# def traverse(root, heights, height=0):
#     if root is None:
#         return
#     if len(heights) < height + 1:
#         heights.append([])
#     heights[height].append(root.val)
#     traverse(root.left, heights, height + 1)
#     traverse(root.right, heights, height + 1)
