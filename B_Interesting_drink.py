from bisect import bisect_right
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
q = int(input())

a.sort()
for _ in range(q):
    m = int(input())
    left,right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] >= m+1:
            right = mid - 1
        else:
            left = mid + 1
    print(left)
    # print(bisect_right(a,m))