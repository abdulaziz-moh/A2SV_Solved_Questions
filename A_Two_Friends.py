t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    for i in range(n):
        if p[p[i]-1] == i+1:
            print(2)
            break
    else:        
        print(3)