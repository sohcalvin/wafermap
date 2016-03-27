from flask_restful import Resource
from flask import url_for
import os
import json
from models.wafermap import WaferMap



class WaferFinder(Resource) :

    def __init__(self, **kwargs):
        self.data_dir = kwargs["data_dir"]

    def get(self, wafer_id=None):
        if(wafer_id is None) :
            return self.getWaferList()

        # waferFile = "wafer{0}".format(wafer_id)
        waferFile = wafer_id
        waferFilePath = os.path.join(self.data_dir,waferFile)
        waferMap = WaferMap.load(waferFilePath)
        return waferMap.jsonData()

    def getWaferList(self):
        waferFiles = [ f for f in os.listdir(self.data_dir) if(os.path.isfile(os.path.join(self.data_dir, f))) ]
        waferFiles.sort(key=lambda s : int(s.split('_')[-1])) # numeric sort by the waferid extension
        return [ {"name" : w, "url" : url_for("map", wafer_id = w)} for w in waferFiles]
        # return [ {"name" : w, "url" : url_for("map", wafer_id= int(w[5:]))} for w in waferFiles]
