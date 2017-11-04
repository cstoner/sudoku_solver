from .sudokuElement import SudokuElement


class SudokuGrid:
    """SudokuGrid represents a 9x9 sudoku grid"""
    GRID_SIZE = 9
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
            assert(len(grid_elem) == self.GRID_SIZE)

            for (col_idx, elem) in enumerate(grid_elem):
                self.set((row_idx, col_idx), elem)
            row_idx += 1

    def _load_grid_from_file(self, filename):
        with open(filename) as fd:
            grid_data = fd.read()
        self._load_grid_from_string(grid_data)

    def _load_empty_grid(self):
        for i in range(self.GRID_SIZE):
            self._grid.append([SudokuElement()] * self.GRID_SIZE)

    def get(self, pos):
        x, y = pos
        return self._grid[x][y].val

    def set(self, pos, val):
        assert (val == "" or 1 <= int(val) <= self.GRID_SIZE)
        x, y = pos
        self._grid[x][y] = SudokuElement(val)

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
