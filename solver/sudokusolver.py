class SudokuSolver:
    def __init__(self, sudoku_grid):
        self.grid = sudoku_grid

    def solve(self):
        solved_new_entry = True
        while solved_new_entry:
            solved_new_entry = False
            for col in range(self.grid.GRID_SIZE):
                for row in range(self.grid.GRID_SIZE):
                    if self.grid.get(col, row) is None:
                        valid_numbers = self.grid.get_valid_numbers(col, row)
                        # If there's only 1 valid number, then we should enter it
                        if len(valid_numbers) == 1:
                            self.grid.set(col, row, next(iter(valid_numbers)))
                            solved_new_entry = True
                            continue

                        # Check the valid numbers for this square against the numbers that could be filled into other
                        # squares. If we have one that could not be placed anywhere else, we should place it
                        empty_nodes_in_region = self.grid.get_empty_neighbors(col, row)
                        remaining_numbers = set()
                        for elem in empty_nodes_in_region:
                            remaining_numbers.update(elem.get_valid_numbers())

                        for candidate_number in valid_numbers:
                            if candidate_number not in remaining_numbers:
                                self.grid.set(col, row, next(iter(valid_numbers)))
                                solved_new_entry = True
                                continue

        return self.grid
