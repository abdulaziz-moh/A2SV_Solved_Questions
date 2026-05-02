import sys
input = sys.stdin.readline


def findmex(arrset,n):
    for i in range(n+1):
        if i not in arrset:
            return i


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    visited = set()
    ans = []
    while arr != sorted(arr):
        idx = findmex(set(arr), n)
        if  idx != n:
            arr[idx] = idx
            visited.add(idx)
            ans.append(idx+1)
        else:
            x = 0
            for i in range(n+1):
                if i not in visited:
                    x = i
                    break
            ans.append(x+1)
            arr[x] = n
    
    print(len(ans))
    print(*ans)
                  

def main():

    t = int(input()) 
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
