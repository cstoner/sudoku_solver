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
        self._grid = [[SudokuElement()]*self.GRID_SIZE for _ in range(self.GRID_SIZE)]

    def get(self, col, row):
        return self._grid[col][row].val

    def set(self, col, row, val):
        assert (val is None or 1 <= int(val) <= self.GRID_SIZE)
        if not (val is None):
            self._check_row_constraint(row, val)
            self._check_col_constraint(col, val)
            self._check_subregion_constraint(col, row, val)
        self._grid[col][row] = SudokuElement(val)

    def _check_row_constraint(self, row, val):
        """Ensures that the passed row does not already contain an element with a value of val"""
        if val is None:
            return
        for col in range(self.GRID_SIZE):
            if self.get(col, row) == val:
                raise SudokuError(
                    "An element of value '{}' already exists at position ({}, {})".format(val, col, row)
                )

    def _check_col_constraint(self, col, val):
        """Ensures that the passed column does not already contain an element with a value of val"""
        if val is None:
            return
        for row in range(self.GRID_SIZE):
            if self.get(col, row) == val:
                raise SudokuError(
                    "An element of value '{}' already exists at position ({}, {})".format(val, col, row)
                )

    def _check_subregion_constraint(self, col, row, val):
        """Ensures that a value does not exist in the same sub-region as (col, row)"""
        if val is None:
            return

        starting_col = (col // self.SUBREGION_SIZE) * self.SUBREGION_SIZE
        starting_row = (row // self.SUBREGION_SIZE) * self.SUBREGION_SIZE

        for col in range(starting_col, starting_col + self.SUBREGION_SIZE):
            for row in range(starting_row, starting_row + self.SUBREGION_SIZE):
                if self.get(col, row) == val:
                    raise SudokuError(
                        "An element of value '{}' already exists at position ({}, {})".format(val, col, row)
                    )

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
