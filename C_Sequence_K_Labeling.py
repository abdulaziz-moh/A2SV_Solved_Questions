from collections import defaultdict
import sys
from typing import Counter
input = sys.stdin.readline

def solve():

    a, k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    count = Counter(arr)

    if k < max(count.values()):
        print('NO')
        return
    putval = defaultdict(list)
    c = 0
    for key in count:
        # c = 1
        for _ in range(count[key]):
            putval[key].append(c%k + 1)
            c += 1
    ans = []
    for v in arr:
        ans.append(putval[v].pop())
    print('YES')
    print(*ans)

def main():
    # Handle multiple test cases (standard for Codeforces)
    t = 1
    # t = int(input())  # Uncomment if problem has multiple test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
