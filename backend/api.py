from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

DATA = {}

class Data(Resource):
    def get(self, data_id):
        return {data_id: DATA[data_id]}
    
    def put(self, data_id):
        DATA[data_id] = request.form["data"]
        return {data_id: DATA[data_id]}

    def delete(self, data_id):
        del DATA[data_id]

class AllData(Resource):
    def get(self):
        return DATA
    
    def post(self):
        data_id = int(max(DATA.keys()))+1
        DATA[data_id] = request.form["data"]
        return {data_id: DATA[data_id]}

api.add_resource(AllData, "/data")
api.add_resource(Data, "/data/<string:data_id>")

if __name__ == "__main__":
    app.run(debug=True)

