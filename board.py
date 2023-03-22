class BoardException(Exception):
    pass

class Board:
    def __init__(self, input_file):
        self.board_text = []
        self.board = []
        self.input_file = input_file

    def read_from_input_file(self):
        with open(self.input_file, "r") as f:
            file = f.read()
            self.board_text = list(file.replace('\n', ''))
    
    def print_board_text(self, board):
        counter = 0
        print("-" * 94)
        for square in board:
            square = set(square)
            if len(square) != 1:
                square = ''.join(list(square))
            elif len(square) == 1:
                square = list(square)[0]
            if counter == 27 or counter == 54:
                print('|\n', "-" * 94, sep="")
            elif counter % 9 == 0 and counter != 0:
                print('|')
            if square == '.' or square == ' ' or square == '0':
                square = ' '
            if counter % 3 == 0:
                print("|", end='')
            print("|", end='')
            print(square, ' ' * (9 - len(square)), end = "", sep="")
            counter += 1
        print('|')
        print("-" * 94)

    def print_board_solved(self):
        board = self.board
        counter = 0
        print("-" * 19, end='')
        for cell in board:
            if counter % 9 == 0:
                print('\n', end='')
            if counter % 3 == 0:
                print('|', end='')
            print(cell, end = '')
            counter += 1
        print('\n', "-" * 19, sep='')

    def convert_to_options(self):
        for square in self.board_text:
            if square == '.':
                options = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            else:
                options = set(square)
            self.board.append(options)

    def get_row(self, row_num):
        if row_num < 0 or row_num > 8:
            raise BoardException(f'Row {row_num} does not exist')

        start = row_num * 9
        end = start + 9
        row = self.board[start:end]

        if len(row) != 9:
            raise BoardException(f'Row must have length 9. Row has length {len(row)}')
        return row

    def get_col(self, col_num):
        if col_num < 0 or col_num > 8:
            raise BoardException(f'Col {col_num} does not exist')

        col = []
        i = col_num
        while i < 81:
            col.append(self.board[i])
            i += 9

        if len(col) != 9:
            raise BoardException(f'Col must have length 9. Column has length {len(col)}')
        return col

    def get_3x3(self, square_num):
        if square_num < 0 or square_num > 8:
            raise BoardException(f'Square {square_num} does not exist')

        starting_idx = [0, 3, 6, 27, 30, 33, 54, 57, 60]
        square = []

        i = starting_idx[square_num]
        while i < 81 and len(square) < 9:
            for j in range(3):
                square.append(self.board[i])
                i += 1
            i += 6

        if len(square) != 9:
            raise BoardException(f'3 X 3 square must have length 9. Currently has length {len(square)}')
        return square

    def set_row(self, row_num, row):
        if row_num < 0 or row_num > 8:
            raise BoardException(f'Row {row_num} does not exist')
        if len(row) != 9:
            raise BoardException(f'Row must have length 9. Row has length {len(row)}')

        start = row_num * 9
        end = start + 9
        self.board[start:end] = row
    
    def set_col(self, col_num, col):
        if col_num < 0 or col_num > 8:
            raise BoardException(f'Column {col_num} does not exist')
        if len(col) != 9:
            raise BoardException(f'Column must have length 9. Column has length {len(col)}')

        i = col_num
        j = 0
        while i < 81 and j < 9:
            self.board[i] = col[j]
            i += 9
            j += 1

    def set_3x3(self, square_num, square):
        if square_num < 0 or square_num > 8:
            raise BoardException(f'Square {square_num} does not exist')
        if len(square) != 9:
            raise BoardException(f'Square must have length 9. Square has length {len(square)}')

        starting_idx = [0, 3, 6, 27, 30, 33, 54, 57, 60]

        i = starting_idx[square_num]
        k = 0
        while i < 81 and k < 9:
            
            for j in range(3):
                self.board[i] = square[k]
                i += 1
                k += 1
            i += 6

    def get_board_size(self):
        counter = 0
        for cell in self.board:
            counter += len(cell)
        return counter

    def get_empty_cells_cnt(self):
        counter = 0
        for cell in self.board:
            if len(cell) != 1:
                counter += 1
        return counter
        