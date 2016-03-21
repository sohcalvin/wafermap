from flask import Flask, send_from_directory
from flask_restful import Resource, Api
from controller.wafer_finder import WaferFinder
from controller.wafer_predictor import WaferPredictor
import os

app = Flask(__name__)
api = Api(app)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(ROOT_DIR,"frontend")
DATA_DIR = os.path.join(ROOT_DIR,"../../data")


@app.route('/app/<path:path>')
def serve_page(path):
    # print("Serving file : ",APP_DIR,"/" ,path)
    return send_from_directory( APP_DIR, path)

api.add_resource(WaferFinder, '/map/<int:wafer_id>', endpoint='map', resource_class_kwargs={ 'data_dir': DATA_DIR })
api.add_resource(WaferFinder, '/map', endpoint='maplist', resource_class_kwargs={ 'data_dir': DATA_DIR })
api.add_resource(WaferPredictor, '/wafer_predictor', endpoint='wafer_predictor', resource_class_kwargs={ 'data_dir': DATA_DIR })


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0' port=8080, debug=True)
