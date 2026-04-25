class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for a,b in prerequisites:
            pre[a].append(b)
        
        visited = [-1 for _ in range(numCourses)]
        def havecycle(vertice):
            
            for v in pre[vertice]:
                if visited[v] == 0:
                    return True
                elif visited[v] == -1:
                    visited[v] = 0
                    if havecycle(v):
                        return True
                    visited[v] = 1
            return False
        for i in range(numCourses):
            if visited[i] == -1:
                if havecycle(i):
                    return False
        return True