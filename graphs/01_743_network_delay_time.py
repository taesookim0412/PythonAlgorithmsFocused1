import collections
import heapq
from typing import List


def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    edges = collections.defaultdict(list)
    for time in times:
        src, dest, weight = time
        edges[src].append([dest, weight])
    visited = {}
    pq = [[0, k]]
    while pq:
        dist, src = heapq.heappop(pq)
        if src in visited:
            continue
        visited[src] = dist
        for target, weight in edges[src]:
            if target not in visited:
                heapq.heappush(pq, [dist + weight, target])
    return max(visited.values()) if len(visited) == n else -1


networkDelayTime('', [[2,1,1],[2,3,1],[3,4,1]],
4,
2)