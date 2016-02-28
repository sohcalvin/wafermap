from flask import Flask, send_from_directory
from flask_restful import Resource, Api
from controller.wafer_finder import WaferFinder
import os

app = Flask(__name__)
api = Api(app)

ROOT_DIR = os.getcwd()
APP_DIR = os.path.join(ROOT_DIR,'src/webapp')

@app.route('/app/<path:path>')
def serve_page(path):
    print(APP_DIR,"/" ,path)
    return send_from_directory( APP_DIR, path)

api.add_resource(WaferFinder, '/map/<int:wafer_id>', endpoint='cv', resource_class_kwargs={ 'data_dir': 'data' })

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0' port=8080, debug=True)
