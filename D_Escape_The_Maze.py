import sys
from collections import deque
input = sys.stdin.readline

def solve():
    input()  # blank line separator
    n, k = map(int, input().split())
    friends = list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # Multi-source BFS from all friends
    dist_f = [-1] * (n + 1)
    q = deque()
    for x in friends:
        dist_f[x] = 0
        q.append(x)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist_f[v] == -1:
                dist_f[v] = dist_f[u] + 1
                q.append(v)

    # BFS from node 1, only through safe nodes
    dist_v = [-1] * (n + 1)
    dist_v[1] = 0
    visited = [False] * (n + 1)
    visited[1] = True
    q = deque([1])
    found = False

    while q and not found:
        u = q.popleft()
        # Leaf check: degree 1, not room 1
        if u != 1 and len(adj[u]) == 1:
            found = True
            break
        for v in adj[u]:
            if not visited[v]:
                d = dist_v[u] + 1
                if d < dist_f[v]:   # Vlad arrives strictly before any friend
                    dist_v[v] = d
                    visited[v] = True
                    q.append(v)

    print("YES" if found else "NO")

t = int(input())
for _ in range(t):
    solve()