"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        n = len(employees)
        imp, graph = defaultdict(int), defaultdict(list)
        for emp in employees: 
            graph[emp.id] = emp.subordinates
            imp[emp.id] = emp.importance 
        
        visited = set([id])
        def dfs(vertice):
            if not graph[vertice]:
                return imp[vertice]
            
            sm = 0
            for v in graph[vertice]:
                if v not in visited:
                    visited.add(v)
                    sm += dfs(v)
            return imp[vertice] + sm
        return dfs(id)
        