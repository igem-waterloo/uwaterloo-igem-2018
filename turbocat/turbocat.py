from flask import Flask, json, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def turbocat():
    return 'Hello, World!'

@app.route('/results')
def results():
    data = [
      {'name': '0m', 'percent': 50},
      {'name': '15m', 'percent': 60},
      {'name': '30m', 'percent': 65},
      {'name': '45m', 'percent': 60},
      {'name': '60m', 'percent': 50},
      {'name': '75m', 'percent': 45},
      {'name': '90m', 'percent': 50},
    ];
    return jsonify(data)

@app.route('/set_ratio', methods=['POST'])
def set_ratio():
    ratio = json.loads(request.data).get('ratio')

    return ratio
