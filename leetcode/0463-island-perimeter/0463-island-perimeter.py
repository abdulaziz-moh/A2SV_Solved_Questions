class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(col)] for j in range(row)]

        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
    
        def findisland(i,j):
            
            visited[i][j] = True
            perimeter = 0
            for row_change, col_change in directions:
                r = i + row_change
                c = j + col_change

                if not inbound(r,c) or grid[r][c] == 0:
                    perimeter += 1

                elif not visited[r][c]:
                    perimeter += findisland(r,c)

            return perimeter

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return findisland(i,j)