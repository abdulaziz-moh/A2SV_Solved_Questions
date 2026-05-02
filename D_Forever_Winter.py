from collections import Counter, deque
import sys
input = sys.stdin.readline

def solve():

    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    count = [0]*(n+1)
    for i in range(1,n+1):
        count[i] = len(adj[i]) 
        
    cnt = Counter(count)
    del cnt[0]
    x,y = 0,0
    if len(cnt) == 1:
        for k in cnt:
            x,y = k,k
    elif len(cnt) == 2:
        mx = max(cnt.keys())
        x,y = mx, mx
    elif len(cnt) == 3:
        mn = (0,float('inf'))
        for k,v in cnt.items():
            if v == 1:
                x = k
            else:
                a,b = mn
                if v < b:
                    mn = (k,v)
        a,b = mn
        y = a
    print(x,y-1)



def main():

    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
