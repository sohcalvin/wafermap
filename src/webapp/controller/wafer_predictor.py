from flask_restful import Resource
from flask import url_for, request
import os
import json
from models.wafermap import WaferMap



class WaferPredictor(Resource) :

    def __init__(self, **kwargs):
        self.data_dir = kwargs["data_dir"]

    def post(self):
        json_data = request.get_json(force=True)
        coord = [k.split(",") for k in json_data["mapData"].keys()]
        mapLine = self.coordToMap(coord)
        print(mapLine)
        return 'Todo', 200


    def coordToMap(self, arrayOfCoord):
        print(arrayOfCoord)
        rows = 100;
        cols = 100;
        map = [0] * (rows * cols)
        for xy in arrayOfCoord :
            x = int(xy[0])
            y = int(xy[1])
            # print(x, ",", y)
            idx = (y * cols) + x
            map[idx] = 1
        return map