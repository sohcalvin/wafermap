import numpy as np

class WaferMap(object) :
    def __init__(self):
        print("init ...")
        self.body = None
        self.pattern = None


    def __str__(self):
        if(self.body is None) :
            return "Map body is empty"
        else :
            return str(self.body)

    def initMap(self, row, col, pattern=None):
        self.body = np.zeros([row,col])
        if(pattern is not None) :
            self._markPattern(pattern)

    def _markPattern(self, pattern):
        for row, col in pattern :
            # row, col = i
            self.body[row][col] = 1





