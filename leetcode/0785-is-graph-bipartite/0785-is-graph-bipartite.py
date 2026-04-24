class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        visited = [-1] * n
        # visited[0] = 1
        
        def dfs(vertex):

            for neighbour in graph[vertex]:
                if visited[neighbour] == -1:
                    visited[neighbour] = abs(1-visited[vertex])
                    found = dfs(neighbour)
                    if not found:
                        return found
                elif visited[neighbour] == visited[vertex]:
                    return False
            return True
    
        for i in range(n):
            if visited[i] == -1:
                visited[i] = 1
                if not dfs(i):
                    print(i)
                    return False

        return True