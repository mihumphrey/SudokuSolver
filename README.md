# Sudoku Solver

This sudoku solver will solve any puzzle. It first uses the rules of the game to isolate and solve cells. 

This is enough to solve most easy to medium-hard puzzles. For very complex puzzles, however, these rules do not solve every puzzle. 

For this reason, if an iteration of finding cells through the rules of the puzzle does not find any new cells, a recursive backtracking algorithm will brute force a solution, thus guaranteeing a solution to every puzzle.
<hr>

## Rule Based Solutions
This solver treats defines each cell as a list of candidate numbers (1-9) that a cell can possibly be with the following constraints.

- Any cell with more than one candidate is unknown and needs to be solved for. 

- Any cell with only one candidate is considered solved, and thus does not need to be solved for.

- Any cell with no candidates indicates an invalid board.
<hr>

### Single Hidden Cell Finder
A single hidden cell is a cell which is the only cell in a given row, column, or 3x3 grid that has some candidate number. If this is found, this cell can simply be solved. 

Once solved, each cell in that row, column, and 3x3 grid loses that number as a candidate.
<hr>

### Single Naked Cell Finder
A single naked cell is a cell which only has one candidate. If this is found, this cell can simply be solved with that value.

Once solved, each cell in that row, column, and 3x3 grid loses that number as a candidate.
<hr>

### Exclusive 3x3 Grid Solver
An exclusive 3x3 grid solver will examine toe 1x3 columns of each 3x3 grid. 

If one of the rows/columns is the only column within that 3x3 grid to contain some candidate, then that candidate must be in that row/column, and the rest of the row/column outside of that 3x3 grid must NOT contain that candidate, so it may be removed.
<hr>

### Subset/Identical Pairs Solver
A subset/identical pair solver is when 2 cells within a row/column/3x3 grid contain the same 2 candidates, and NO other candidates. 

If this is found, these candidates may be removed from every other cell in the row/column/3x3 grid. 

This expands of course to identical trios, quads, etc.
<hr>

## Brute Force Solution

The brute force solution uses a backtracking algorithm to recursively attempt to solve each cell. If an invalid board is found, we backtrack and try another value. This guarantees a solution at the expense of time complexity. 

The time complexity of this algorithm is O(9<sup>m</sup>). This is why the rule-based solution is run until exhaustion to lower *m* as far as possible.

Of course, since *m* must be much < 81, this exponential growth is bounded. Thus, a solution must exist.