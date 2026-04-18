t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    a.sort()
    sum = 0
    for i in range(6):
        sum += (a[i]*(-1))
    sum += a[-1]
    print(sum)