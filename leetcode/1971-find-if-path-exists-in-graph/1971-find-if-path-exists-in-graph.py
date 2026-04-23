class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False for _ in range(n)]
        def dfs(vertex):
            if vertex == destination:
                return True

            visited[vertex] = True
            for i in graph[vertex]:
                if not visited[i]:
                    found = dfs(i)
                    if found:
                        return found
            return False
        return dfs(source)