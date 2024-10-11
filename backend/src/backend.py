from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():
    text = request.json['text']
    return jsonify({'text' : text})


@app.route('/indexing', methods=['POST'])
def indexing():
    text = request.json['text']
    return jsonify({'text' : text})