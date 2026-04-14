class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def validoptions(idx):
            row, col = idx
            all = {"1","9","8","3","4","2","5","6","7"}
            all -= set(board[row])
            all -= set(board[i][col] for i in range(9))

            start_row, start_col = (row // 3) * 3, (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    all.discard(board[i][j])
            return list(all)

        idxarr = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    idxarr.append([i,j])

        def backtrack(idx):
            if idx == len(idxarr):
                return True
            
            valid = validoptions(idxarr[idx])
            if not valid:
                return False
            for v in valid:
                a, b = idxarr[idx]
                board[a][b] = v
                if backtrack(idx + 1):
                    return True
                board[a][b] = "." 

        backtrack(0)
                
            

            
