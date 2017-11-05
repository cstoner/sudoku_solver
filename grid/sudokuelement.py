class SudokuElement:
    """This class exists to pretty-print and input sudoku values"""

    def __init__(self, grid_size, val=None):
        if (val is None) or (type(val) is str and val.strip() == ''):
            self.val = None
            self.valid_numbers = set(range(1, grid_size+1))
        else:
            self.val = int(val)
            self.valid_numbers = []

    def get_valid_numbers(self):
        return self.valid_numbers

    def invalidate_number(self, value):
        if int(value) in self.valid_numbers:
            self.valid_numbers.remove(int(value))

    def __str__(self):
        if self.val is None:
            return ' '
        else:
            return str(self.val)

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