class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## is valid row
        ## is valid column
        ## is valid 3x3
        rows = len(board)
        cols = len(board) ## rows and cols are same value

        for i in range(rows):
            seen = set()
            curr_row = board[i]
            for j in curr_row:
                if j in seen:
                    return False
                if j != ".":
                    seen.add(j)

        for i in range(cols):
            seen = set()
            for j in range(rows):
                if board[j][i] in seen:
                    return False
                if board[j][i] != ".":
                    seen.add(board[j][i])
    
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        curr_box = board[r][c]
                        if curr_box in seen:
                            return False
                        if curr_box != ".":
                            seen.add(curr_box)
        
        return True

        