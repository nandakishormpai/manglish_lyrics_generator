from numpy import result_type
from flask import Flask,request,jsonify
from model_files.ml_predict import generate,Model
import pickle

app = Flask("manglish_lyrics_generation")

@app.route('/', methods=['POST'])
def predict():
    model = Model()
    lyrics = generate(model)
    response = {
        "lyrics": lyrics
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)