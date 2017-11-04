#!/usr/bin/env python3
import argparse

from grid import SudokuGrid


def get_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file', metavar='FILE', type=str, help='sudoku puzzle to load')

    return parser


def main(cli_args):
    grid = SudokuGrid(cli_args.file)
    print(grid)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    main(args)