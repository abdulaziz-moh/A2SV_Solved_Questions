class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for v in edges:
            a,b = v
            graph[a].append(b)
            graph[b].append(a)
        
        self.ans = False
        # print(graph)
        def dfs(vertice, visited):
            neighbours = graph[vertice]

            if vertice == destination:
                self.ans = True
                return
            if not neighbours:
                return

            visited.add(vertice)
            for v in neighbours:
                if v not in visited:
                    dfs(v, visited)

        dfs(source, set())
        return self.ans
