from flask import Flask, request, jsonify
import json
from os import path


app = Flask(__name__)
data = []


if path.isfile('log.json') is False:
    with open('log.json','w') as f:
        f.write("[]")
        print("Created blank log file.")

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
    new_data = request.form
    print("The data I recieved: "+str(new_data))
    with open("log.json") as f:
        data = json.load(f)
    data.append({"Timestamp": new_data['Timestamp'], "Project": new_data['Project'], "Category": new_data['Category']})
    with open("log.json",'w') as f:
        json.dump(data, f)
    return jsonify(data)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)