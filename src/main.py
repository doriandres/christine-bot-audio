from flask import Flask, request, Response, jsonify
from .helpers.request_helper import read_audio
from .helpers.files_helper import clean_files
from .utils.wav_converter import convert_to_wav
from .utils.audio_recognizer import recognize_audio

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "I'm alive";

@app.route('/', methods=['POST'])
def run():
    print("Processing audio")
    try:
        print("Reading audio file")
        filename = read_audio(request)

        print("Converting to wav file")
        convert_to_wav(filename)

        print("Converting to text")
        text = recognize_audio(filename)

        print("Cleaning files")
        clean_files(filename)

        return jsonify(text=text)
    except Exception as err:
        print("Could not process audio", err)
        return Response(status=500)
