class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, graph = len(isConnected), defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        count, visited = 0, [False] * n
        def dfs(vertex):
            
            for v in graph[vertex]:
                if not visited[v]:
                    visited[v] = True
                    dfs(v)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                count += 1
                dfs(i)
        return count

