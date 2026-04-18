
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    w = input()
    target = 0
    for v in w:
        target += (ord(v) - ord('a'))
    find = 0
    for i in range(m - 1):
        find += (ord(s[i])  - ord('a'))
        
    left = 0
    for i in range(m-1, n):
        find += (ord(s[i]) - ord('a'))
        # print(find, " ", target)
        if find == target:
            print('YES')
            break
        find -= (ord(s[left]) - ord('a'))
        left += 1
    else:
        print('NO')
    