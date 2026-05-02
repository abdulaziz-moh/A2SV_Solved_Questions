import sys
from collections import Counter, deque

input = sys.stdin.readline

def solve():
    n = int(input())

    adj = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    a = list(map(int, input().split()))

    pos = [0]*(n+1)
    for i in range(n):
        pos[a[i]] = i
    
    for i in range(1,n+1):
        adj[i].sort(key = lambda x:pos[x])

    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])

    bfs = []    
    while queue:

        u = queue.popleft()
        bfs.append(u)
        
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


    if bfs != a:
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    solve()
    
    
    
    
    
# import sys
# from collections import deque

# def solve():
#     # Use fast I/O
#     input = sys.stdin.read().split()
#     if not input:
#         return
    
#     ptr = 0
#     n = int(input[ptr])
#     ptr += 1

#     adj = [[] for _ in range(n + 1)]
#     for _ in range(n - 1):
#         u = int(input[ptr])
#         v = int(input[ptr + 1])
#         adj[u].append(v)
#         adj[v].append(u)
#         ptr += 2
    
#     # The sequence to validate
#     a = [int(x) for x in input[ptr:]]
    
#     # 1. Start must be node 1
#     if a[0] != 1:
#         print("No")
#         return

#     # 2. Map each node to its position in the given sequence
#     pos = [0] * (n + 1)
#     for i in range(n):
#         pos[a[i]] = i
        
#     # 3. Sort neighbors of each node by their 'pos' in sequence 'a'
#     # This ensures BFS explores neighbors in the order they appear in 'a'
#     for i in range(1, n + 1):
#         adj[i].sort(key=lambda x: pos[x])

#     # 4. Perform standard BFS
#     bfs_order = []
#     visited = [False] * (n + 1)
#     queue = deque([1])
#     visited[1] = True
    
#     while queue:
#         u = queue.popleft()
#         bfs_order.append(u)
#         for v in adj[u]:
#             if not visited[v]:
#                 visited[v] = True
#                 queue.append(v)

#     # 5. Compare result
#     if bfs_order == a:
#         print("Yes")
#     else:
#         print("No")

# if __name__ == "__main__":
#     solve()