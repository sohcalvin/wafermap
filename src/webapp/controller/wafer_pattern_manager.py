from flask_restful import Resource
from flask import url_for, request
import numpy as np
import os
import json

class WaferPatternManager(Resource) :

    def __init__(self, **kwargs):
        self.data_dir = kwargs["data_dir"]

    def post(self):
        json_data = request.get_json(force=True)
        pattern_name = json_data.get("patternName")
        coord = [k.split(",") for k in json_data["mapData"].keys()]
        coord = [ [int(i), int(j) ] for i,j in coord]
        if(pattern_name is None) :
            return "patternName required", 400
        pattern_file_path = os.path.join(self.data_dir, "patterns", pattern_name +".pattern")
        with open(pattern_file_path, 'w') as outfile:
            json.dump(coord, outfile)
        return coord, 200


    def coordToMap(self, arrayOfCoord):
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