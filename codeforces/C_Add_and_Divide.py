def countsteps(a, b):
    if b <= 1:
        return float('inf')
    s = 0
    while a > 0:
        a //= b
        s += 1
    return s

def solve(a, b):
    best = float('inf')
    for inc in range(100):
        b_try = b + inc
        if b_try < 2:
            continue
        total = inc + countsteps(a, b_try)
        best = min(best, total)
        if countsteps(a, b_try) <= 1:
            break                   
    return best

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))