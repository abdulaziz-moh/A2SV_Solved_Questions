class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        n = len(values)
        graph = defaultdict(list)
        for i in range(n):
            a,b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        
        # self.ans = -1.00000
        def dfs(node, target, ans):
            if node == target:
                self.ans = ans
                return
            
            for v, val in graph[node]:
                if v not in visited:
                    visited.add(v)
                    dfs(v, target, ans * val)
            return
        retval = []
        for node, target in queries:
            visited = set()
            self.ans = -1.00000
            
            if node in graph and target in graph:
                dfs(node,target, 1)
            retval.append(self.ans)
                    
        return retval