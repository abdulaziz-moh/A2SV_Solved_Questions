from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solve():
    input()
    n, k = map(int, input().strip().split())
    graph = defaultdict(set)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
        
    queue = deque(set())
    
    for i in range(n+1):
        if len(graph[i]) <= 1:
            queue.append(i)

    while k > 0 and queue:
        newqueue = deque()
        
        while queue:
            v = queue.pop()
            x = graph[v].pop() if graph[v] else None
            if x in graph:
                graph[x].discard(v)
                        
            if v in graph:
                del graph[v]
            
            if x in graph and len(graph[x]) <= 1:
                newqueue.append(x)

        if not graph:
            break
        
        queue = deque(set(newqueue))
        k -= 1

    print(len(graph))


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()