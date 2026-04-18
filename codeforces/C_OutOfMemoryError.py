# t = int(input())
# for _ in range(t):
#     n, m, h = map(int, input().split())
#     a = list(map(int, input().split()))
#     arr = []
#     for _ in range(m):
#         arr.append(list(map(int, input().split())))
        
#     last_crash_idx = -1
#     current_state = {}
    
#     for i in range(m):
#         idx, val = arr[i]
#         idx -= 1
        
#         curr_val = current_state.get(idx, a[idx]) + val
#         if curr_val > h:
#             last_crash_idx = i
#             current_state = {}
#         else:
#             current_state[idx] = curr_val
#     for i in range(last_crash_idx + 1, m):
#         idx, val = arr[i]
#         idx -= 1
#         a[idx] += val
#     print(*a)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t = int(next(it))
    
    results = []
    
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        h = int(next(it))
        
        a = [int(next(it)) for _ in range(n)]
        
        arr = []
        for _ in range(m):
            arr.append((int(next(it)), int(next(it))))
            
        last_crash_idx = -1
        current_state = {}
        
        for i in range(m):
            idx_raw, val = arr[i]
            idx = idx_raw - 1
            
            curr_val = current_state.get(idx, a[idx]) + val
            if curr_val > h:
                last_crash_idx = i
                current_state = {}
            else:
                current_state[idx] = curr_val
        
        for i in range(last_crash_idx + 1, m):
            idx_raw, val = arr[i]
            a[idx_raw - 1] += val
            
        results.append(" ".join(map(str, a)))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()