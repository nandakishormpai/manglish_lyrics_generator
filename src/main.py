from flask import Flask,jsonify
from model_files.ml_predict import generate,Model


app = Flask("manglish_lyrics_generation")

@app.route('/', methods=['GET'])
def predict():
    model = Model()
    lyrics = generate(model)
    response = {
        "lyrics": lyrics
    }
    response = jsonify(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)