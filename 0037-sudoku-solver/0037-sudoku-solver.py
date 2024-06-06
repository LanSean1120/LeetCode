class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(sudoku, row, col, num):
            '''row'''
            if num in sudoku[row]:
                return False

            '''col'''
            for r in range(9):
                if sudoku[r][col] == num:
                    return False
            '''box'''
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if sudoku[start_row + i][start_col + j] == num:
                        return False
            return True
            
        def find_empty_cell(sudoku):
            for i in range(9):
                for j in range(9):
                    if sudoku[i][j] == ".":
                        return i, j
            return None, None
        def sol_sudoku(sudoku):
            row, col = find_empty_cell(sudoku)
            if row == None:
                return True
            for num in range(1,10):
                if is_valid(sudoku, row, col, str(num)):
                    sudoku[row][col] = str(num)
                    if sol_sudoku(sudoku):
                        return True
                    sudoku[row][col] = "."
            return False
        sol_sudoku(board)