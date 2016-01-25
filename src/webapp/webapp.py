from flask import Flask, send_from_directory
import os
from models.wafermap import WaferMap
import json

ROOT_DIR = os.getcwd()
app = Flask(__name__,static_url_path='')

@app.route('/app/<path:path>')
def send_js(path):
    print(path)
    return send_from_directory(os.path.join(ROOT_DIR,'src/webapp'), path)

@app.route('/map/<int:wafer_id>')
def getMap(wafer_id) :
    waferFile = "wafer{0}".format(wafer_id)
    # waferFilePath = os.path.join(ROOT_DIR,"data",waferFile)
    waferFilePath = os.path.join("data",waferFile)
    print(waferFilePath)
    waferMap = WaferMap.load(waferFilePath)
    print(waferMap.jsonData())
    return json.dumps(waferMap.jsonData())

if __name__ == '__main__':
    app.run()