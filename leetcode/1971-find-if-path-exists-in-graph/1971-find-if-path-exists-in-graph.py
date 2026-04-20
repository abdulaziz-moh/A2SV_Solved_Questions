class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(vertice, visited):

            if vertice == destination:
                return True

            visited[vertice] = True
            for v in graph[vertice]:
                if not visited[v]:
                    found = dfs(v, visited)
                    if found:
                        return True

            return False

        visited  = [False for _ in range(n)]
        return dfs(source, visited)
