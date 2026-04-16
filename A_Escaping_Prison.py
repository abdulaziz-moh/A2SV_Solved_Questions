t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    sum = 0
    for _ in range(n):
        sum += max(map(int, input().split()))
    if sum >= h:
        print('YES')
    else:
        print('NO')
    