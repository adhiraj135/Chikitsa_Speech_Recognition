from flask import Flask, render_template, request, jsonify, send_file

import os
import base64
from io import BytesIO

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save_audio', methods=['POST'])
def save_audio():
    audio_data = request.json['audio_data']
    audio_bytes = base64.b64decode(audio_data)

    with open('static/recorded audios/recorded_audio.wav', 'wb') as audio_file:
        audio_file.write(audio_bytes)

    return jsonify({'message': 'Audio saved successfully'})


@app.route('/get_audio', methods=['GET'])
def get_audio(request,response):
    # return send_file('recorded_audio.wav', as_attachment=True)
    response.json("hello")

if __name__ == '__main__':
    app.run(debug=True)
