import os
from unittest import TestCase

from grid import SudokuGrid
from solver import SudokuSolver


class TestSudokuSolver(TestCase):
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_RESOURCES_DIR = "../resources"

    def test_solve_easy_sudoku_1(self):
        solution = """2 7 5|9 3 8|1 4 6
6 9 4|2 5 1|3 7 8
3 1 8|7 4 6|5 2 9
-----+-----+-----
4 6 3|1 9 5|7 8 2
8 2 9|3 6 7|4 5 1
7 5 1|8 2 4|6 9 3
-----+-----+-----
5 3 6|4 8 2|9 1 7
1 4 2|6 7 9|8 3 5
9 8 7|5 1 3|2 6 4"""
        grid = SudokuGrid(os.path.join(self.THIS_DIR, self.TEST_RESOURCES_DIR, "easy_sudoku_1.txt"))
        solver = SudokuSolver(grid)

        solved_grid = solver.solve()
        self.assertEqual(solution, str(solved_grid))

