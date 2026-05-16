import math

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    
    if m >= 2 and math.ceil(n / m) <= n - k - 1:
        print("YES")
    else:
        print("NO")