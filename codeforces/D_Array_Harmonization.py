t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = [1] + list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    a.sort()
    res = 0 
    print(a)
    print(b)

    j = 0
    matches= 0
    for x in a:
        while j < n and b[j] <= x:
            j += 1
        if j < n :
            matches += 1
            j += 1
    res += (n - matches)
    print (res)


















# from typing import Counter

# t = int(input())

# def find(val, count):
#     x = sorted(count.values())
#     print(x)
#     # x.sort()
#     for v in x:
#         if val > v:
#             count[v] -= 1
#             if count[v] == 0:
#                 del count[v]
#             return True
#     return False


# for _ in range(t):
#     n, m = map(int, input().split())
#     a = [1]
#     a.extend(list(map(int,input().split())))
#     b = list(map(int,input().split()))
    
#     count = Counter(a)
   
#     cnt = 0
#     for v in b:
#         if find(v, count):
#             cnt += 1
#     print(cnt)
    
    

