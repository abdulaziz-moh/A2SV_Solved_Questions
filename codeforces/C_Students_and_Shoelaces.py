from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solve():

    n, m = map(int, input().strip().split())
    graph = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
        
    cnt = 0
    queue = deque()
    
    for i in range(n+1):
        if len(graph[i]) == 1:
            queue.append(i)

    while queue:

        newqueue = deque()
        while queue:
            v = queue.pop()
            if v in graph:
                del graph[v]
            for k, g in graph.items():
                g.discard(v)

        for k,g in graph.items():
            if len(g) == 1:
                newqueue.append(k)

        cnt += 1
        # queue = deque(set(newqueue))
        queue = newqueue
    print(cnt)


def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()