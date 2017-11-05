Overview
========
This is a very simple sudoku solver that I wrote because someone on /r/learnpython was asking about projects to learn
python, and I said that one of my first projects was a sudoku solver.

They asked for the source, but I didn't have it any more due to a few computer switches

Usage
=====
You should just pass a file containing a csv representation of a sudoku grid to solve

    ./main.py FILE

Unit tests can be ran as follows

    python -m unittest

Goals of the Project
====================
I wanted to try a few things in python that I hadn't really bothered to fiddle with much in the past:

* Python OOP: Normally, I don't bother with OOP python, but this seemed like a good candidate
* Learn PyCharm: In the past, I'd always just used a simple text editor, like Sublime Text or Atom or something
  but since I've been using IntelliJ at work, it seemed like PyCharm would be a good fit
* `unittest` module: I hadn't bothered learning much of the python unit test framework before, so this seemed like
  a good opportunity. The tests are pretty atrocious and certainly not comprehensive, but they still were invaluable
  during development

Approach
========
The approach used is not powerful enough to solve all sudoku, but should be capable of solving a good chunk of them.

Essentially, it just keeps track of what numbers are valid for a given sudoku square, and if there is only one
option available, then it inserts that one. It will also check to see if a number can only legally be placed in a single
subregion of the sudoku grid.

The process is continued until all of the squares are filled in.

Improvements
============
A number of improvements could be made:
1. Instead of iterating over the whole grid looking for entries to fill in, it would be better to only look at the
   empty ones. They could be kept in a queue which could be cycled through until completion.
2. There's certainly a bit more code duplication than I'd like.
3. The project is a bit confused about whether sudoku values are strings or integers. It'd probably make sense to
   generalize things a bit to potentially support 16x16 sudoku grids.
