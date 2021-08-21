import collections

# graph: {
#   0: [1, 2],
#   1: [0, 2, 3],
#   2: [0, 1],
#   3: [1]
# }
# A: 0
# B: 3
# Output: 2
def length_of_shortest_path(graph: Dict[int, List[int]], a: int, b: int) -> int:
    q = collections.deque([a])
    # WRITE YOUR BRILLIANT CODE HERE
    visited = set()
    length = 0
    while q:
        for i in range(len(q)):
        #curr = a
            curr = q.popleft()
            if curr == b:
                return length
            for neighbor in graph[curr]:
                if neighbor in visited:
                    continue
                q.append(neighbor)
                visited.add(neighbor)
        length += 1
    return 0

length_of_shortest_path()

