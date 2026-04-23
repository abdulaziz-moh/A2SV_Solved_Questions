class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False for _ in range(n)]
        stack = [source]
        visited[source] = True

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            for v in graph[node]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True
        return False