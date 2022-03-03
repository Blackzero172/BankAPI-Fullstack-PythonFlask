from flask_cors import CORS
from mongoengine import *
from flask import Flask
from bson.objectid import ObjectId
import json

db = connect("BankAPI")

app = Flask(__name__)
CORS(app)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)

        return super().default(o)


app.json_encoder = CustomJSONEncoder
import user.routes
if __name__ == "__main__":
    app.run(debug=True)
