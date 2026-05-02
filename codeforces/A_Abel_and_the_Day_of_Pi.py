import math
import sys
input = sys.stdin.readline

def solve():
    s = input()
    cnt = 0
    pi = "314159265358979323846264338327"
    
    for i in range(len(s)-1):
        if s[i] != pi[i]:
            break
        cnt += 1
    print(cnt)
    
    
def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
