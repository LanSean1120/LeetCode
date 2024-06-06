class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = [board[i][j] for i in range(9) for j in range(9)]
        def is_valid(board):
            '''row'''
            for i in range(0,81,9):
                for j in range(1,10):
                    if board[i:i+9].count(str(j))>1:
                        return False
            '''col'''
            for i in range(9):
                for j in range(1,10):
                    if board[i:i+81:9].count(str(j))>1:
                        return False
            '''box'''
            for i in range(0, 81, 27):
                for j in range(i, i+6+1, 3):
                    box_temp = []
                    for k in range(j, j+18+1, 9):
                        box_temp += board[k:k+3]
                    for j in range(1,10):
                        if box_temp.count(str(j))>1:
                            return False
            return True
        return is_valid(sudoku)