from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

DATA_FILE = "/mnt/data/contador.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {"gato": 0, "perro": 0}

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/api/contador", methods=["GET"])
def get_contador():
    data = load_data()
    return jsonify(data)

@app.route("/api/contador/gato", methods=["POST"])
def increment_gato():
    data = load_data()
    data["gato"] += 1
    save_data(data)
    return jsonify(data)

@app.route("/api/contador/perro", methods=["POST"])
def increment_perro():
    data = load_data()
    data["perro"] += 1
    save_data(data)
    return jsonify(data)

@app.route("/")
def hello():
    return "Hola desde el BACKEND Flask"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

