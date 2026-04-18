import math


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int,input().split()))
    a = list(map(int,input().split()))
    
    if sum(a) > k:
        print(-1)
        continue

    left, right = 1, 5 * (10**8)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        sm = sum(math.ceil(dis/mid) * time for dis, time in zip(d,a))
        if sm <= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
    