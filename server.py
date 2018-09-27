#!flask/bin/python
from flask import Flask, jsonify, make_response, request
from nlp_annotator import Annotator

#web app
app = Flask(__name__)

#create annotator
annotator = Annotator()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/analyze', methods=['POST'])
def get_tasks():
    #text = request.args.get("text")

    json = request.get_json(force=True)
    text = json["text"]
    lang = json["lang"]

    annotations = annotator.analyze(text, lang)

    return jsonify({
        "text":text,
        "annotations": annotations
        })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5500)