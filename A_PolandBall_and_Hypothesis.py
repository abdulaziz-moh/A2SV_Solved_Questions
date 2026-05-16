n = int(input())
status = False
for i in range(1,1001):
    x = (n * i) + 1
    r = x// 2
    for j in range(2,r+1):
        if x / j == x // j:
            print(i)
            status = True
            break
    if status:
        break
    