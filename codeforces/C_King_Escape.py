import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def solve():
    n = int(input())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    
    grid = [[1]*n for _ in range(n)]
    for i in range(n):
        grid[ax - 1][i] = 0
        grid[i][ay - 1] = 0
        
        
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1,-1), (-1,1), (1,-1), (1,1)]
    def inbound(row, col):
        return (0 <= row < n and 0 <= col < n)
    
    x,y = ax-1, ay-1
    while inbound(x,y):
        grid[x][y] = 0
        x, y = x + 1, y + 1
    x,y = ax-1, ay-1
    while inbound(x,y):
        grid[x][y] = 0
        x, y = x + 1, y - 1
    x,y = ax-1, ay-1
    while inbound(x,y):
        grid[x][y] = 0
        x, y = x - 1, y - 1
    x,y = ax-1, ay-1
    while inbound(x,y):
        grid[x][y] = 0
        x, y = x - 1, y + 1
        
    def dfs(row, col):
        if row == cx-1 and col == cy-1:
            return True

        grid[row][col] = '0'
        
        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change

            if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                find = dfs(new_row, new_col)
                if find:
                    return True
        return False
    
    if dfs(bx-1,by-1):
        print('YES')
    else:
        print('NO')


def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
    
