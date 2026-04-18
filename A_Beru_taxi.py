import math
import sys
input = sys.stdin.readline

a,b = map(int, input().split())
n = int(input())
ans = float("inf")
for _ in range(n):
    x,y,v = map(int,input().split())
    ans = min(ans, math.sqrt(((x-a)**2) + ((y-b)**2)) / v)

print(ans)