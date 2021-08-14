def level_order_traversal(root: Node) -> List[List[int]]:
    res = []
    traverse(root, res)
    return res


def traverse(root, heights, height=0):
    if root is None:
        return
    if len(heights) < height + 1:
        heights.append([])
    heights[height].append(root.val)
    traverse(root.left, heights, height + 1)
    traverse(root.right, heights, height + 1)
