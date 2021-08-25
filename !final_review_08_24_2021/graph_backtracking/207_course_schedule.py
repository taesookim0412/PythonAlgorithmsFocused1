class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for prereqList in prerequisites:
            course, prereq = prereqList
            graph[course].append(prereq)

        for course in range(numCourses):
            if self.dfs(graph, course, set()):
                return False
        return True

    def dfs(self, graph, src, visited):
        '''returns True if src matches dest'''
        if src in visited:
            return True
        if src not in graph:
            return False
        for dest in graph[src]:
            visited.add(src)
            if self.dfs(graph, dest, visited):
                return True
            visited.remove(src)
        return False