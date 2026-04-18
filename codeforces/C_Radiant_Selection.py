import math


t = int(input())
for _ in range(t):
    k = int(input())
    
    left, right = k, 2*10**18
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        a = mid - math.floor(math.isqrt(mid))

        if a >= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)