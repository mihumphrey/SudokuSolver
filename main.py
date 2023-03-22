
from board import Board
from solver import Solver

import time
            
def generate_board(input_file):
    board = Board(input_file)
    board.read_from_input_file()
    board.convert_to_options()
    board.print_board_text(board.board)
    return board

def main():
    board = generate_board('input/input7.txt')
    solver = Solver(board)
    i = 0
    time_rules_s = time.time()
    while i != -1:
        old_size = solver.board.get_board_size()
        solver.single_naked_values()
        solver.single_hidden_values()

        solver.exclusive_3x3_rows()
        solver.exclusive_3x3_cols()
        
        solver.subsets_rows()
        solver.subsets_cols()
        solver.subsets_3x3s()
        new_size = solver.board.get_board_size()
        # board.print_board_text(board.board)

        if new_size == old_size:
            empty_cells = solver.board.get_empty_cells_cnt()
            print(f'PUZZLE DID NOT CHANGE AFTER {i} ITERATIONS ({(time.time() - time_rules_s) * 1000}ms). STARTING BRUTE FORCE WITH {empty_cells} EMPTY CELLS.')
            solver.board.print_board_text(board.board)
            time_brute_s = time.time()
            solver.brute_force()
            print(f'SPENT {(time.time() - time_brute_s) * 1000}ms on brute-force algorithm')
            solver.board.print_board_text(board.board)
            break
        if solver.is_solved():
            print(f'PUZZLE SOLVED AFTER {i} ITERATIONS.')
            break
        i += 1


if __name__ == "__main__":
    main()