from flask import Flask, request, jsonify
from speech_to_text import transcribe_audio
from parser import parse_ingredients
from converter import convert_to_grams
import os

app = Flask(__name__)
UPLOAD_FOLDER = "../uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_audio():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    text = transcribe_audio(file_path)
    parsed = parse_ingredients(text)
    grams = convert_to_grams(parsed)

    return jsonify({
        "transcription": text,
        "converted": grams
    })

if __name__ == '__main__':
    app.run(debug=True)
 
