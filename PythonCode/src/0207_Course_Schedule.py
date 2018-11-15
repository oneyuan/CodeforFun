class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def makeGraph(numCourses, prerequisites):
            graph = [[] for _ in range(numCourses)]
            for x, y in prerequisites:
                graph[x].append(y)
            return graph

        def dfs(x, visited, graph):
            if visited[x] == 1:
                return True
            elif visited[x] == -1:
                return False
            visited[x] = -1
            for y in graph[x]:
                if not dfs(y, visited, graph):
                    return False
            visited[x] = 1
            return True

        visited = [0 for _ in range(numCourses)]
        graph = makeGraph(numCourses, prerequisites)
        for i in range(numCourses):
            if not dfs(i, visited, graph):
                return False
        return True

    def canFinish0(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def has_cycle(node):
            visited[node] = 2
            for nxt in graph[node]:
                if nxt not in graph:
                    visited[nxt] = 1
                    continue
                if visited[nxt] == 2 or (visited[nxt] == 0 and has_cycle(nxt)):
                    return True
            visited[node] = 1
            return False

        visited = [0] * numCourses
        graph = {}
        for post, pre in prerequisites:
            graph[pre] = graph.get(pre, []) + [post]
        for node in graph:
            if visited[node] == 0:
                if has_cycle(node):
                    return False
                visited[node] = 1
        return True

