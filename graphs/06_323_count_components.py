class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for edge in edges:
            src, dest = edge
            graph[src].append(dest)
            graph[dest].append(src)
        visited = set()
        components = 0
        # A graph not containing a 0th key will add an additional component.
        # So, a 0th key is created using range(n) with an empty dfs.
        # for i in graph.keys():
        for i in range(n):
            if i not in visited:
                self.dfs(graph, i, visited)
                components += 1
        return components
    def dfs(self, graph, src, visited):
        visited.add(src)
        for destination in graph[src]:
            if destination not in visited:
                self.dfs(graph, destination, visited)