class SudokuElement:
    """This class exists to pretty-print and input sudoku values"""

    def __init__(self, val=None):
        val = val.strip()
        if val == '':
            self.val = None
        else:
            self.val = val

    def __str__(self):
        if self.val is None:
            return ' '
        else:
            return self.val
