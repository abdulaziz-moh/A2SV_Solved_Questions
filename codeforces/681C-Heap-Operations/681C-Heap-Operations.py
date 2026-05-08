from heapq import heappush, heapreplace, heappop
import sys
input = sys.stdin.readline

def solve():
    heap = []
    ans = []
    n = int(input())
    for _ in range(n):
        s = input().split()
        
        if s[0] == 'insert':
            ans.append(f'insert {s[1]}')
            heappush(heap, int(s[1]))
        elif s[0] == 'removeMin':
            if not heap:
                ans.append('insert 1')
            else:
                heappop(heap)
            ans.append('removeMin')
        elif s[0] == 'getMin':
            
            mn = int(s[1])
            while heap and heap[0] < mn:
                ans.append('removeMin')
                heappop(heap)
            if not heap or heap[0] > mn:
                heappush(heap, mn)
                ans.append(f'insert {mn}')
            ans.append(f'getMin {mn}')  
    print(len(ans))    
    for v in ans:
        print(v)  

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()