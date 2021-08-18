def zig_zag_traversal(root: Node) -> List[List[int]]:
    res = []
    q = collections.deque([(root, 1)])
    while q:
        level_q = collections.deque()
        for i in range(len(q)):
            curr, height = q.popleft()
            if curr is None:
                continue
            if height % 2 == 0:
                level_q.appendleft(curr.val)
            else:
                level_q.append(curr.val)
            if curr.left:
                q.append([curr.left, height + 1])
            if curr.right:
                q.append([curr.right, height + 1])
        res.append(list(level_q))
    return res