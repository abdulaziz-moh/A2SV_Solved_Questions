from collections import defaultdict, deque


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())

    graph = defaultdict(list)
    degree = [0] * (n + 1)

    for _ in range(n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
        
    queue, cycle = deque(), set([i for i in range(1, n + 1)])

    for i in range(n+1):
        if degree[i] == 1:
            queue.append(i)
            cycle.discard(i)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 1:
                cycle.discard(neighbor)
                queue.append(neighbor)
    dist1, dist2 = [-1] * (n + 1), [-1] * (n + 1)
    
    queue = deque([a])
    dist1[a] = 0
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist1[neighbor] == -1:
                dist1[neighbor] = dist1[node] + 1
                queue.append(neighbor)
    queue = deque([b])
    dist2[b] = 0
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist2[neighbor] == -1:
                dist2[neighbor] = dist2[node] + 1
                queue.append(neighbor)
    
    for v in cycle:
        if dist2[v] < dist1[v]:
            print('YES')
            break
    else:
        print('NO')