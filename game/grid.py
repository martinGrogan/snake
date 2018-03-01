import numpy

MIN_SIZE = 4


class GameGrid:

    def __init__(self, line_num, col_num):
        if line_num < MIN_SIZE or col_num < MIN_SIZE:
            raise TypeError('line and column number should be higher than %d' % MIN_SIZE)

        self.line_num = line_num
        self.col_num = col_num
        self.matrix = numpy.empty((line_num, col_num,), dtype=int)
        self.matrix[:] = int(0)
