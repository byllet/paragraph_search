from flask import Flask, jsonify, request, make_response
import json

from searcher import Searcher


app = Flask(__name__)
searcher = Searcher(collection_name='paragraphs')


def incorrect_params(param):
    return make_response(f'Not found in json: {param}\n', 400)


@app.route('/searching', methods=['POST'])
def searching():
    if 'text' not in request.json:
        return incorrect_params('text')
    if 'top_k' not in request.json:
        return incorrect_params('top_k') 
    
    return json.dumps(searcher.search(text=request.json['text'], top_k=request.json['top_k']), ensure_ascii=False)


@app.route('/indexing', methods=['POST'])
def indexing():
    if 'dataset_name_of_docs' not in request.json:
         return incorrect_params('dataset_name_of_docs')
    
    if searcher.index(request.json['dataset_name_of_docs']) == -1:
        return incorrect_params('content') 
    
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(host='::', port='5000')
