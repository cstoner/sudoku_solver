import math

from grid import SudokuElement, SudokuError


class SudokuGrid:
    """SudokuGrid represents a 9x9 sudoku grid"""
    GRID_SIZE = 9
    SUBREGION_SIZE = int(math.sqrt(GRID_SIZE))

    _grid = []

    def __init__(self, filename=None, str=None):
        self._load_empty_grid()
        if filename is not None:
            self._load_grid_from_file(filename)
        elif str is not None:
            self._load_grid_from_string(str)

    def _load_grid_from_string(self, string):
        grid_rows = string.split("\n")
        assert (len(grid_rows) == self.GRID_SIZE)

        row_idx = 0
        for grid_row in grid_rows:
            grid_elem = grid_row.split(",")
            assert (len(grid_elem) == self.GRID_SIZE)

            for (col_idx, elem) in enumerate(grid_elem):
                if elem.strip() == "":
                    elem = None
                self.set(row_idx, col_idx, elem)
            row_idx += 1

    def _load_grid_from_file(self, filename):
        with open(filename) as fd:
            grid_data = fd.read()
        self._load_grid_from_string(grid_data)

    def _load_empty_grid(self):
        self._grid = []
        for _ in range(self.GRID_SIZE):
            row = []
            for _ in range(self.GRID_SIZE):
                row.append(SudokuElement(self.GRID_SIZE))
            self._grid.append(row)

    def get(self, col, row):
        """Returns the value of the node at (col, row)"""
        return self._grid[col][row].val

    def get_valid_numbers(self, col, row):
        """Returns all of the possible valid numbers that could be entered into (col, row)"""
        return self._grid[col][row].get_valid_numbers()

    def get_empty_neighbors(self, col, row):
        """Returns all of the empty nodes in a sub-region, except for the one at (col, row)"""
        starting_col = (col // self.SUBREGION_SIZE) * self.SUBREGION_SIZE
        starting_row = (row // self.SUBREGION_SIZE) * self.SUBREGION_SIZE
        neighbor_list = []

        for new_col in range(starting_col, starting_col + self.SUBREGION_SIZE):
            for new_row in range(starting_row, starting_row + self.SUBREGION_SIZE):
                if new_col == col and new_row == row:
                    continue
                if self.get(new_col, new_row) is not None:
                    neighbor_list.append(self._grid[col][row])

        return neighbor_list

    def set(self, col, row, val):
        """Sets the item at (col, row) to the specified value"""
        if val is None:
            return
        assert (1 <= int(val) <= self.GRID_SIZE)
        self._check_value_constraint(col, row, val)
        self._grid[col][row] = SudokuElement(self.GRID_SIZE, val)
        self._invalidate_number(col, row, val)

    def _check_value_constraint(self, col, row, val):
        if int(val) not in self._grid[col][row].get_valid_numbers():
            raise SudokuError("An element of value '{}' cannot be placed in ({}, {})".format(val, col, row))

    def _invalidate_number(self, col, row, val):
        if val is None:
            return

        # Invalidate this number along the specified row and column
        for i in range(self.GRID_SIZE):
            self._grid[i][row].invalidate_number(val)
            self._grid[col][i].invalidate_number(val)

        starting_col = (col // self.SUBREGION_SIZE) * self.SUBREGION_SIZE
        starting_row = (row // self.SUBREGION_SIZE) * self.SUBREGION_SIZE
        for col in range(starting_col, starting_col + self.SUBREGION_SIZE):
            for row in range(starting_row, starting_row + self.SUBREGION_SIZE):
                self._grid[col][row].invalidate_number(val)

    def __str__(self):
        GRID_VERTICAL_SEPARATOR = "-----+-----+-----"

        def build_line(grid_line):
            return "{} {} {}|{} {} {}|{} {} {}".format(*grid_line)

        lines = []

        for line in self._grid[:3]:
            lines.append(build_line(line))
        lines.append(GRID_VERTICAL_SEPARATOR)
        for line in self._grid[3:6]:
            lines.append(build_line(line))
        lines.append(GRID_VERTICAL_SEPARATOR)
        for line in self._grid[6:9]:
            lines.append(build_line(line))

        return "\n".join(lines)
