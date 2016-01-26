from flask_restful import Resource
import os
import json
from models.wafermap import WaferMap


class WaferFinder(Resource) :

    def __init__(self, **kwargs):
        self.data_dir = kwargs["data_dir"]

    def get(self, wafer_id):
        waferFile = "wafer{0}".format(wafer_id)
        waferFilePath = os.path.join(self.data_dir,waferFile)
        print(waferFilePath)
        waferMap = WaferMap.load(waferFilePath)
        # jsonString = json.dumps(waferMap.jsonData())
        return waferMap.jsonData()
