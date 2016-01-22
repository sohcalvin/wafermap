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

    def _toString(self):
        pass

    def initMap(self, row, col, pattern=None):
        self.body = np.zeros([row,col])
        if(pattern is not None) :
            self._radomisedMarkPattern(pattern)

    def _radomisedMarkPattern(self,pattern) :
        for i in pattern :
            row,col = i
            offsetRow = np.random.randint(-1,1,1)
            offsetCol = np.random.randint(-1,1,1)
            row += offsetRow
            col += offsetCol
            self.body[row, col] = 1





