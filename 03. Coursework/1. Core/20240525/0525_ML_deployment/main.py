from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/<float:param1>/<float:param2>/<float:param3>/<float:param4>")
def hello_world(param1,param2,param3,param4):

    result = model.predict([[param1,param2,param3,param4]])

    return result.tolist()
