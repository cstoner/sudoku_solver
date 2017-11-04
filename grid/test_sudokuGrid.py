from unittest import TestCase

from grid import SudokuGrid


class TestSudokuGrid(TestCase):
    def test_init_grid(self):
        grid = SudokuGrid()
        for row in grid._grid:
            for col in row:
                assert (col.val is None)

    def test_load_empty_grid(self):
        grid = SudokuGrid("../resources/empty_grid.txt")
        for row in grid._grid:
            for col in row:
                assert (col.val is None)

    def test_load_single_entry_grid_1(self):
        grid = SudokuGrid("../resources/single_entry_grid_1.txt")
        assert (grid.get((0, 0)) == "1")

    def test_load_single_entry_grid_2(self):
        grid = SudokuGrid("../resources/single_entry_grid_2.txt")
        assert (grid.get((8, 8)) == "1")

