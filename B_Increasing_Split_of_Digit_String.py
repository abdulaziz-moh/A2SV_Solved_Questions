t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    
    ans = [int(a[0])]
    x, y = int(a[0]), int(a[1:])
    if x >= y:
        print('NO')
    else:
        print('YES')
        print(2)
        print(x,y)       
