import sys
from types import GeneratorType

# Increase standard recursion depth as a backup
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# --- ADVANCED RECURSION BOILERPLATE ---
def bootstrap(f, stack=[]):
    """Decorator to allow deep recursion using generators."""
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

# --- COMMON DATA STRUCTURES ---
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j: self.parent[root_i] = root_j

# --- MATH UTILS ---
MOD = 10**9 + 7
def gcd(a, b):
    while b: a, b = b, a % b
    return a

# --- SOLUTION LOGIC ---
@bootstrap
def dfs(u, p, adj):
    """Example deep recursion DFS."""
    for v in adj[u]:
        if v != p:
            yield dfs(v, u, adj)
    yield None

def solve():
    # Example: Reading a graph
    # n = int(input())
    # adj = [[] for _ in range(n)]
    # for _ in range(n-1):
    #     u, v = map(int, input().split())
    #     adj[u-1].append(v-1)
    #     adj[v-1].append(u-1)
    # dfs(0, -1, adj)
    pass

def main():
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
