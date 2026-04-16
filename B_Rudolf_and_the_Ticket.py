from bisect import bisect_left


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b.sort()
    c.sort()
    
    ans = 0
    for v in b:
        idx = bisect_left(c, k-v + 1)
        ans += idx
    print(ans)