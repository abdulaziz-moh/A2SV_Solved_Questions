t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
        
    mul, sum = m, 0
    for v in a:
        sum += (mul * v)
        mul -= 1
        if mul <= 0:
            mul = 0
    print(sum)