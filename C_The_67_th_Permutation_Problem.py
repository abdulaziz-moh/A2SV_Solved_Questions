t = int(input())
for _ in range(t):
    n = int(input())

    a = 1
    b = 3*n
    ans = []
    for i in range(n):
        ans.append(b)
        ans.append(b-1)
        b -= 2
        ans.append(a)
        a+= 1
    print(*ans)