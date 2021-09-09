class Solution:
    def isValidSudoku(self, board):
        return self.isValid_row(board) and self.isValid_col(board) and self.isValid_unit(board)

    def isValid_row(self, board):
        for item_row in board:
            num_row = [i for i in item_row if i != "."]
            if len(set(num_row)) != len(num_row):
                return False 
        return True
    
    def isValid_col(self, board):
        for item_col in list(zip(*board)):
            num_col = [i for i in item_col if i != "."]
            if len(set(num_col)) != len(num_col):
                return False
        return True

    
    def isValid_unit(self, board):
        for j in range(0, 7, 3):
            
            for i in range(0, 7, 3):
                print(i,j)
                item_unit = []
                item_unit.extend([board[i][j], board[i+1][j], board[i+2][j],
                    board[i][j+1], board[i+1][j+1], board[i+2][j+1],
                    board[i][j+2], board[i+1][j+2], board[i+2][j+2],
                ]) 
                num_unit = [i for i in item_unit if i != "."]
           
                if len(set(num_unit)) != len(num_unit):
                    return False
            
        return True

print(Solution().isValidSudoku(board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(Solution().isValidSudoku(board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))


print(Solution().isValidSudoku(board = [[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","."]
,[".",".",".",".",".","3",".",".","1"]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]]))
