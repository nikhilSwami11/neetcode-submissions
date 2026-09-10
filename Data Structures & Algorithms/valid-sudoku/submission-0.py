class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid_start = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        n = len(board)
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[i][j]== ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[j][i]== ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for x,y in grid_start:
            seen = set()
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if board[i][j]== ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        return True
