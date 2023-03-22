class Solver:
    def __init__(self, board):
        self.board = board

    def single_naked_values(self):
        self.single_naked_value_rows()
        self.single_naked_value_cols()
        self.single_naked_value_3x3s()

    def single_hidden_values(self): 
        self.single_hidden_value_rows()
        self.single_hidden_value_cols()
        self.single_hidden_value_3x3s()

#######################################################################################################################
#                                                                                                                     #
#                        Below this line are the solutions for the single naked value solvers.                        #
#                                                                                                                     #
#######################################################################################################################
    def single_naked_value_rows(self):
        """
            - Responsible for finding single naked values in a row. 
            - This means that some cell in a row has a single candidate, thus is set to that candidate, 
                and that candidate is removed from all other cells in that row.
            
            - Modifies the board object in place
        """
        for i in range(9):
            row = self.board.get_row(i)
            for element in row:
                if len(element) == 1:
                    num = list(element)[0]
                    for element2 in row:
                        if num in element2 and element != element2:
                            # print(f'REMOVING {num} FROM CELL {element2} ON ROW {i}')
                            element2.discard(num)
            self.board.set_row(i, row)

    def single_naked_value_cols(self):
        """
            - Responsible for finding single naked values in a column. 
            - This means that some cell in a column has a single candidate, thus is set to that candidate, 
                and that candidate is removed from all other cells in that column.
            
            - Modifies the board object in place
        """
        for i in range(9):
            col = self.board.get_col(i)
            for element in col:
                if len(element) == 1:
                    num = list(element)[0]
                    for element2 in col:
                        if num in element2 and element != element2:
                            # print(f'REMOVING {num} FROM CELL {element2} ON COL {i}')
                            element2.discard(num)
            self.board.set_col(i, col)

    def single_naked_value_3x3s(self):
        """
            - Responsible for finding single naked values in a 3x3 square. 
            - This means that some cell in a 3x3 square has a single candidate, thus is set to that candidate, 
                and that candidate is removed from all other cells in that 3x3 square.
            
            - Modifies the board object in place
        """
        for i in range(9):
            square = self.board.get_3x3(i)
            for element in square:
                if len(element) == 1:
                    num = list(element)[0]
                    for element2 in square:
                        if num in element2 and element != element2:
                            # print(f'REMOVING {num} FROM CELL {element2} ON SQUARE {i}')
                            element2.discard(num)
            self.board.set_3x3(i, square)

#######################################################################################################################
#                                                                                                                     #
#                       Below this line are the solutions for the single hidden value solvers.                        #
#                                                                                                                     #
#######################################################################################################################
    def single_hidden_value_rows(self):
        """
            - Responsible for finding single hidden values in a row. 
            - This means that some cell in a row is the only cell in that row with a candidate,
                thus is set to that candidate.

            - Modifies the board object in place
        """
        for i in range(9):
            row = self.board.get_row(i)
            j = 0
            for cell in row:
                for num in cell:
                    contains = False
                    cell2_num = 0
                    for cell2 in row:
                        if num in cell2 and cell2_num != j:
                            contains = True
                        cell2_num += 1
                    if len(cell) > 1 and not contains:
                        # print(f'SETTING CELL {cell} TO {set(num)} ON ROW {i}')
                        cell = set(num)
                        row[j] = cell
                j += 1

            
            self.board.set_row(i, row)          

    def single_hidden_value_cols(self):
        """
            - Responsible for finding single hidden values in a column. 
            - This means that some cell in a column is the only cell in that column with a candidate,
                thus is set to that candidate.
                
            - Modifies the board object in place
        """
        for i in range(9):
            col = self.board.get_col(i)
            j = 0
            for cell in col:
                for num in cell:
                    contains = False
                    cell2_num = 0
                    for cell2 in col:
                        if num in cell2 and cell2_num != j:
                            contains = True
                            break
                        cell2_num += 1
                    if not contains and len(cell) > 1:
                        # print(f'SETTING CELL {cell} TO {set(num)} ON COL {i}')
                        cell = set(num)
                        col[j] = cell
                j += 1
            
            self.board.set_col(i, col)   

    def single_hidden_value_3x3s(self):
        """
            - Responsible for finding single hidden values in a 3x3 square. 
            - This means that some cell in a 3x3 square is the only cell in that 3x3 square with a candidate,
                thus is set to that candidate.
                
            - Modifies the board object in place
        """
        for i in range(9):
            square = self.board.get_3x3(i)
            j = 0
            for cell in square:
                for num in cell:
                    contains = False
                    cell2_num = 0
                    for cell2 in square:
                        if num in cell2 and cell2_num != j:
                            contains = True
                        cell2_num += 1
                    if len(cell) > 1 and not contains:
                        # print(f'SETTING CELL {cell} TO {set(num)} ON SQUARE {i}')
                        cell = set(num)
                        square[j] = cell
                j += 1
            
            self.board.set_3x3(i, square)      


#######################################################################################################################
#                                                                                                                     #
#                         Below this line are the solutions for the exclusive region solvers.                         #
#                                                                                                                     #
#######################################################################################################################
    def exclusive_3x3_rows(self):
        """
            - Responsible for handling exclusive regions for 3x3 squares.
            - This means that if one row of a 3x3 square is the only row in the 
                square with some candidate, all other cells in that whole row 
                lose that number as a candidate

            - Modifies the board object in place
        """
        for i in range(9):
            square = self.board.get_3x3(i)
            rows = [square[:3], square[3:6], square[6:9]]
            if i < 3:
                start = 0
            elif i < 6:
                start = 3
            else:
                start = 6
            j = 0
            for row in rows:
                for cell in row:
                    if len(cell) == 1:
                        continue
                    for num in cell:
                        contains = False
                        for row2 in rows:
                            if row == row2:
                                continue
                            for cell2 in row2:
                                if num in cell2:
                                    contains = True
                                    break
                            if contains:
                                break
                        if not contains:
                            rownum = start + j
                            row_to_remove = self.board.get_row(rownum)
                            for cell_to_remove in row_to_remove:
                                if cell_to_remove not in row and num in cell_to_remove:
                                    # print(f'EXCLUSIVE ROW REMOVING {num} FROM CELL {cell_to_remove} IN SQUARE {i}, ROW {rownum}')
                                    cell_to_remove.discard(num)
                j += 1
            self.board.set_3x3(i, square)   

    def exclusive_3x3_cols(self):
        """
            - Responsible for handling exclusive regions for 3x3 squares.
            - This means that if one column of a 3x3 square is the only column in the 
                square with some candidate, all other cells in that whole column 
                lose that number as a candidate

            - Modifies the board object in place
        """
        for i in range(9):
            square = self.board.get_3x3(i)
            cols = [square[0:7:3], square[1:8:3], square[2:9:3]]
            if i % 3 == 0:
                start = 0
            elif i % 3 == 1:
                start = 3
            elif i % 3 == 2:
                start = 6
            j = 0
            for col in cols:
                for cell in col:
                    if len(cell) == 1:
                        continue
                    for num in cell:
                        contains = False
                        for col2 in cols:
                            if col == col2:
                                continue
                            for cell2 in col2:
                                if num in cell2:
                                    contains = True
                                    break
                            if contains:
                                break
                        if not contains:
                            colnum = start + j
                            col_to_remove = self.board.get_col(colnum)
                            for cell_to_remove in col_to_remove:
                                if cell_to_remove not in col and num in cell_to_remove:
                                    # print(f'EXCLUSIVE COL REMOVING {num} FROM CELL {cell_to_remove} IN SQUARE {i}, ROW {i}')
                                    cell_to_remove.discard(num)
                j += 1
            self.board.set_3x3(i, square)  

#######################################################################################################################
#                                                                                                                     #
#                       Below this line are the solutions for the identical candidates solvers.                       #
#                                                                                                                     #
#######################################################################################################################
    def subsets_rows(self):
        """
            - Responsible for checking for pairs, trios, and quads along the same row
            - If a 2 cells contain the same 2 candidates, and only those candidates, 
                they are the only cells with those candidates. Each cell in the row 
                gets that candidate removed.
        """
        for i in range(9):
            row = self.board.get_row(i)  
            cell_num = 0
            for cell in row:
                length = len(cell)
                if length == 1:
                    continue
                cell2_num = 0
                counter = 0
                for cell2 in row:
                    # might need more here. works as is but can miss when subsets exist.
                    if (cell == cell2):
                        counter += 1
                    cell2_num += 1
                if counter == length:
                    for num in cell:
                        for cell2 in row:
                            if num in cell2 and cell2 != cell:
                                # print(f'SUBSET ROW REMOVING {num} FROM {cell2} ON ROW {i}')
                                cell2.remove(num)
                cell_num += 1

    def subsets_cols(self):
        """
            - Responsible for checking for pairs, trios, and quads along the same column
            - If a 2 cells contain the same 2 candidates, and only those candidates, 
                they are the only cells with those candidates. Each cell in the column 
                gets that candidate removed.
        """
        for i in range(9):
            col = self.board.get_col(i)  
            cell_num = 0
            for cell in col:
                length = len(cell)
                if length == 1:
                    continue
                cell2_num = 0
                counter = 0
                for cell2 in col:
                    # might need more here. works as is but can miss when subsets exist.
                    if (cell == cell2):
                        counter += 1
                    cell2_num += 1
                if counter == length:
                    for num in cell:
                        for cell2 in col:
                            if num in cell2 and cell2 != cell:
                                # print(f'SUBSET COL REMOVING {num} FROM {cell2} ON COL {i}')
                                cell2.remove(num)
                cell_num += 1

    def subsets_3x3s(self):
        """
            - Responsible for checking for pairs, trios, and quads along the same 3x3 square
            - If a 2 cells contain the same 2 candidates, and only those candidates, 
                they are the only cells with those candidates. Each cell in the 3x3 square 
                gets that candidate removed.
        """
        for i in range(9):
            square = self.board.get_3x3(i)  
            cell_num = 0
            for cell in square:
                length = len(cell)
                if length == 1:
                    continue
                cell2_num = 0
                counter = 0
                for cell2 in square:
                    # might need more here. works as is but can miss when subsets exist.
                    if (cell == cell2):
                        counter += 1
                    cell2_num += 1
                if counter == length:
                    for num in cell:
                        for cell2 in square:
                            if num in cell2 and cell2 != cell:
                                # print(f'SUBSET SQUARE REMOVING {num} FROM {cell2} ON SQUARE {i}')
                                cell2.remove(num)
                cell_num += 1

    def invalid_board(self):
        """
            - If any cell has zero candidates, something very bad has happened. 
            - Currently not used.
        """
        for cell in self.board.board:
            if len(cell) == 0:
                return False
        return True

    def is_solved(self):
        """
            - If every cell has only one candidate, the board is solved, assuming the board is not invalid.
        """
        for cell in self.board.board:
            if len(cell) != 1:
                return False
        return True

#######################################################################################################################
#                                                                                                                     #
#                            Everything below this line is for the brute force solution.                              #
#                                                        Bleh                                                         #
#                                                                                                                     #
#######################################################################################################################
    def valid(self, row, col, square, value):
        """
            - For the brute force solution, the board is invalid if any value is found in more than one cell.
            - Should probably be combined with invalid_board(self).
        """
        row_count = 0
        col_count = 0
        square_count = 0

        for cell in row:
            if len(cell) == 1 and value in cell:
                row_count += 1
        
        for cell in col:
            if len(cell) == 1 and value in cell:
                col_count += 1

        for cell in square:
            if len(cell) == 1 and value in cell:
                square_count += 1

        if row_count >= 1 or col_count >= 1 or square_count >= 1:
            return False
        return True
        

    def brute_solve(self, board, depth):
        """
            - Recursive backtracking algorithm to guarantee a solution when the logic solution won't work.
            - Steps:
                1. Find a cell to test. 
                    1.1. If no cell found, success.
                2. 
        """
        cell = -1
        for i in range(81):
            if len(board[i]) > 1:
                cell = i
                break

        if cell == -1:
            return True

        rownum = cell // 9
        colnum = cell % 9
        start_i = rownum - rownum % 3 
        start_j = colnum - colnum % 3

        square_start = start_i * 9 + start_j
        starting_idx = [0, 3, 6, 27, 30, 33, 54, 57, 60]
        squarenum = -1
        for i in range(len(starting_idx)):
            if starting_idx[i] == square_start:
                squarenum = i
                break

        row = self.board.get_row(rownum)
        col = self.board.get_col(colnum)
        square = self.board.get_3x3(squarenum)

        old_cell = board[cell]
        for num in range(len(board[cell])):
            if self.valid(row, col, square, list(board[cell])[num]):
                board[cell] = set(list(board[cell])[num])
                if self.brute_solve(board, depth + 1):
                    return True
                board[cell] = old_cell
        return False

    def brute_force(self):
        board = self.board.board 
        self.brute_solve(board, 0)


