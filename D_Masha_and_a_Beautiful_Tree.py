import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    pair = []
    if n <= 1:
        print(0)
        return
    for i in range(0,n,2):
        if abs(arr[i] - arr[i+1]) != 1:
            print(-1)
            return
        pair.append([arr[i]])
        pair.append([arr[i+1]])
        
    count = 0
    while len(pair[0]) != n:
        newpair = []
        for i in range(0,len(pair),2):
            if pair[i][0] > pair[i+1][0]:
                pair[i][0], pair[i+1][0] = pair[i+1][0], pair[i][0]
                count += 1
            if pair[i+1][0] != (pair[i][0] + len(pair[i])):
                print(-1)
                return
            newpair.append(pair[i] + pair[i+1])
        pair = newpair
    print(count)
def main():
    # Handle multiple test cases (standard for Codeforces)
    # t = 1
    t = int(input())  # Uncomment if problem has multiple test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
