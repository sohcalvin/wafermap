import numpy as np
import pickle

class WaferMap(object) :
    def __init__(self, id, title=None):
        print("init ...")
        self.body = None
        self.id = id
        self.title = title
        self.pattern = None


    def __str__(self):
        if(self.body is None) :
            return "Map body is empty"
        else :
             return str(self.body)
    def getBody(self):
        return self.body

    def _toString(self):
        pass

    def initMap(self, row, col, pattern=None):
        self.xDim = col
        self.yDim = row
        self.body = np.zeros([row,col])
        if(pattern is not None) :
            self._radomisedMarkPattern(pattern)

    def _radomisedMarkPattern(self,pattern) :
        for i in pattern :
            row,col = i
            offsetRow = np.random.randint(-2,2,1)
            offsetCol = np.random.randint(-2,2,1)
            row += offsetRow
            col += offsetCol
            self.body[row, col] = 1

    def jsonData(self, title=None):
        json = {}
        json["id"]=self.id
        json["title"] = self.title
        json["xDim"] = self.xDim
        json["yDim"] = self.yDim
        bin1Cells = []
        json["bindata"] = { "1" : bin1Cells}

        for y in range(0,self.yDim) :
            for x in range(0, self.xDim) :
                binValue = self.body[y][x]
                if(binValue == 1) :
                    bin1Cells.append({"x" : x, "y" : y})
        return json;

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
            f.close()

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            wafermap = pickle.load(f)
            f.close()
            return wafermap;





