from flask import Flask, request, jsonify
import json
from os import path


app = Flask(__name__)
data = []


if path.isfile('log.json') is False:
    with open('log.json','w') as f:
        f.write("[]")
        print("Created blank log file.")

# TODO: open file and load data

@app.route("/")
def hello():
    return "Hello World"

@app.route("/get", methods=["GET"])
def get_data():
    with open('log.json','r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/post", methods=["POST"])
def add_data():
    new_data = request.get_json(force=True)
    with open("log.json") as f:
        data = json.load(f)
    data.append({"Timestamp": new_data['timestamp'], "Project": new_data['proj'], "Category": new_data['cat']})
    with open("log.json",'w') as f:
        json.dump(data, f)
    return jsonify(data)


if __name__=="__main__":
    app.run()