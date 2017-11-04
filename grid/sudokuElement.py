class SudokuElement:
    """This class exists to pretty-print and input sudoku values"""

    def __init__(self, val=None):
        if (val is None) or (type(val) is str and val.strip() == ''):
            self.val = None
        else:
            self.val = int(val)

    def __str__(self):
        if self.val is None:
            return ' '
        else:
            return self.val

    def __eq__(self, other):
        if other is SudokuElement:
            return self.val == other.val
        elif other is None:
            return self.val is None
        elif type(other) is int:
            return self.val is not None and other == int(self.val)
        elif type(other) is str:
            return (other.strip() == self.val) or (other.strip() == '' and self.val is None)
        else:
            raise TypeError("Unable to compare a SudokuElement to {}".format(repr(other)))