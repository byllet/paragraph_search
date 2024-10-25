from flask import Flask, jsonify, request, make_response

from paragraphs import indexing_data
from find import find_top_k


app = Flask(__name__)


def incorrect_params(param):
    return make_response(f'Not found in json: {param}\n', 400)


@app.route('/searching', methods=['POST'])
def searching():
    if 'text' not in request.json:
        return incorrect_params('text')
    if 'top_k' not in request.json:
        return incorrect_params('top_k') 
    
    return find_top_k(text=request.json['text'], top_k=request.json['top_k'])


@app.route('/indexing', methods=['POST'])
def indexing():
    if 'dataset_name_of_docs' not in request.json:
         return incorrect_params('dataset_name_of_docs')
    
    for doc in request.json['dataset_name_of_docs']:
        if 'content' not in doc:
            return incorrect_params('content')

        indexing_data(doc['content'])
    
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(host='::', port='5000')
