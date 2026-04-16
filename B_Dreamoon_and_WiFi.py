from typing import Counter

s1 = input()
s2 = input()

target, curr = Counter(s1), Counter(s2)
cnt = 0
depth = curr['?']

def dfs(ch):
    global cnt
    curr[ch] += 1

    if curr['+'] == target['+'] and curr['-'] == target['-']:
        cnt += 1
    
    elif curr['+'] < target['+'] and curr['-'] < target['-']:
        dfs('-')
        dfs('+')
    elif curr['+'] < target['+']:
        dfs('+')
    elif curr['-'] < target['-']:
        dfs('-')
    
    curr[ch] -= 1
    return



if curr['+'] > target['+'] or curr['-'] > target['-']:
    print(float(0))
    exit(0)
dfs(-1)
print(cnt / (2**depth))