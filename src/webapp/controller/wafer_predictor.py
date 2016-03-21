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
        coord = [k for k in json_data["mapData"].keys()]
        self.coordToMap(coord)
        return 'Todo', 200


    def coordToMap(self, arrayOfCoord):
        
        pass