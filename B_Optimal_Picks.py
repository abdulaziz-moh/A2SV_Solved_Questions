import sys
input = sys.stdin.readline

def solve():

    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    
    for i in range(1,n,2):
        inc = a[i-1] - a[i]
        if b - inc >= 0:
            a[i] += inc
            b -= inc
        else:
            a[i] += b
            b = 0
        if b <= 0:
            break
    # print("b",b)
        # if a[i] + b >= a[i-1]:
        #     a[i] = a[i-1]
        # else:
        #     a[i] += b
    # print(a)
    one, two = 0,0
    for i in range(0,n,2):
        one += a[i]
    for i in range(1,n,2):
        two += a[i]
        
    print(one - two)
    
   

def main():
    # Handle multiple test cases (standard for Codeforces)
    # t = 1
    t = int(input())  # Uncomment if problem has multiple test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
# 