t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n-1):
        for j in range(i+1, n):
            a[j] = a[j]^a[i]
    print(a[-1])