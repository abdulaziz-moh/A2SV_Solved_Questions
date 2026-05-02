import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    first = input()
    second = input()
    f,s = [],[]
    for i in range(n):
        f.append(first[i])
        s.append(second[i])
    cnt = 0
    for i in range(n):
        if s[i] == '1':
            if f[i] == '0':
                f[i] = '2'
                cnt += 1
            elif i-1 >= 0 and f[i-1] == '1':
                f[i-1] = '2'
                cnt += 1
            elif i+1 < n and f[i+1] == '1':
                f[i+1] = '2'
                cnt += 1
            
    print(cnt)

def main():

    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
