import sys
from collections import deque

# Increase recursion depth for deep graphs/trees
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    # 1. Input: Nodes (n) and Edges (m)
    try:
        n, m = map(int, input().split())
    except ValueError: return

    # 2. Convert Edge List to Adjacency List
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u) # Omit for directed graphs

    visited_dfs = [False] * (n + 1)

    # 3. DFS - Recursive
    def dfs(u):
        visited_dfs[u] = True
        for v in adj[u]:
            if not visited_dfs[v]:
                dfs(v)

    # 4. BFS - Iterative
    def bfs(start_node):
        dist = [-1] * (n + 1)
        queue = deque([start_node])
        dist[start_node] = 0
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        return dist

if __name__ == "__main__":
    solve()