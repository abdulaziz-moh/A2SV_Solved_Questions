from bisect import bisect_left
from cmath import inf
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.append(-2000000000)
    b.sort()

    for i in range(n):
        
        idx = bisect_left(b, a[i] + a[i-1])
        x = a[i]
        if idx < m:
            x = b[idx] - a[i]
        if x < a[i] or (x > a[i] and a[i] < a[i-1]):
            a[i] = x            
            
        if a[i] < a[i-1]:
            print('NO')
            break 

    else:
        print('YES')

def main():

    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()