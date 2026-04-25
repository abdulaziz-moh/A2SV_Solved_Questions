import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    
    # Read space-separated integers
    # a, b = map(int, input().split())
    
    # Read a list of integers
    arr = list(map(int, input().split()))
    
    arr.sort()
    l,r = 0, n-1
    sm = 0
    while l < r:
        
        sm += ((arr[l] + arr[r]) ** 2)
        l += 1
        r -= 1
    print(sm)
    

def main():
    # Handle multiple test cases (standard for Codeforces)
    t = 1
    # t = int(input())  # Uncomment if problem has multiple test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
