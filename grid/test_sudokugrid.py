#!/bin/env python3
import os
import unittest

from grid import SudokuGrid, SudokuError


class TestSudokuGrid(unittest.TestCase):
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_RESOURCES_DIR = "../resources"

    def test_init_grid(self):
        grid = SudokuGrid()
        for col in range(grid.GRID_SIZE):
            for row in range(grid.GRID_SIZE):
                self.assertTrue(grid.get(col, row) is None,
                                "Element at ({},{}) was not None".format(col, row)
                                )

    def test_load_empty_grid(self):
        grid = SudokuGrid(os.path.join(self.THIS_DIR, self.TEST_RESOURCES_DIR, "empty_grid.txt"))
        for col in range(grid.GRID_SIZE):
            for row in range(grid.GRID_SIZE):
                self.assertTrue(grid.get(col, row) is None,
                                "Element at ({},{}) was not None".format(col, row)
                                )

    def test_load_single_entry_grid_1(self):
        grid = SudokuGrid(os.path.join(self.THIS_DIR, self.TEST_RESOURCES_DIR, "single_entry_grid_1.txt"))
        self.assertTrue(grid.get(0, 0) == 1)

    def test_load_single_entry_grid_2(self):
        grid = SudokuGrid(os.path.join(self.THIS_DIR, self.TEST_RESOURCES_DIR, "single_entry_grid_2.txt"))
        self.assertTrue(grid.get(8, 8) == 1)

    def test_load_easy_sudoku_1(self):
        grid = SudokuGrid(os.path.join(self.THIS_DIR, self.TEST_RESOURCES_DIR, "easy_sudoku_1.txt"))
        self.assertEquals(grid.get_valid_numbers(0, 1), {7})

    def test_row_constraints(self):
        grid = SudokuGrid()
        grid.set(0, 0, 1)
        for x in range(grid.GRID_SIZE):
            try:
                grid.set(x, 0, 1)
                self.fail("Trying to assign a 1 to ({}, {}) should have resulted in an exception".format(x, 0))
            except SudokuError:
                pass

    def test_col_constraints(self):
        grid = SudokuGrid()
        grid.set(0, 0, 1)
        for y in range(grid.GRID_SIZE):
            try:
                grid.set(0, y, 1)
                self.fail("Trying to assign a 1 to ({}, {}) should have resulted in an exception".format(0, y))
            except SudokuError:
                pass

    def test_subregion_constraints(self):
        grid = SudokuGrid()
        grid.set(1, 1, 1)
        for (x, y) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            try:
                grid.set(x, y, 1)
                self.fail("Trying to assign a 1 to ({}, {}) should have resulted in an exception".format(x, y))
            except SudokuError:
                pass


if __name__ == '__main__':
    unittest.main()
