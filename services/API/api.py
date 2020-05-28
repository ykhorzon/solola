# add root_path 
import os, sys
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)

from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, emit, send
from pytube import YouTube
import main
# import ffmpeg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# Routing part
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api/v1/transcription/',  methods=['POST'])
def transcribe():
    # create a socket to real-time response progress
    return jsonify(hello="world")


@socketio.on('connect')
def connect():
    emit('connected', {
        'status': 'connected',
        'response': 'connection is successful'
    })


@socketio.on('transcribe')
def start_transcription(req):

    emit('transcriptionStarted', {
        'status': 'triggered',
        'response': 'transcription is started',
        'stage': '0/4'})
    
    # start to download youtube video
    emit('transcriptionStarted', {
        'status': 'videoDownloadStarted',
        'response': 'youtube video start to be downloaded',
        'stage': '0/4'})
    # clear format
    audio_file_name = 'HASHED'
    VIDEO_PATH = "E:\workplace\projects\solola\solola\services\\videos"
    videos = YouTube(req['yt_url'])
    stream = videos.streams.filter(progressive=True, file_extension='mp4')[0]
    stream.download(output_path = VIDEO_PATH, filename = audio_file_name, filename_prefix = 'raw_')

    emit('transcriptionStarted', {
        'status': 'videoDownloaded',
        'response': 'youtube video is downloaded',
        'stage': '1/4'})


    # mp4 tp wav
    emit('transcriptionStarted', {
        'status': 'videoToAudioConvertionStarted',
        'response': 'youtube video start to convert to audio',
        'stage': '1/4'})
    
    emit('transcriptionStarted', {
        'status': 'videoToAudioConverted',
        'response': 'youtube video is converted to audio',
        'stage': '2/4'})

    # emit('videoToAudioConverted', {'status': 'youtube video is converted to audio', 'stage': '3/4'})

    # run solola
    # TODO
    audio_file_path = 'E:\workplace\projects\solola\solola\services\\videos\\raw_HASHED.mp4'
    output_dir = 'E:\workplace\projects\solola\solola\services\mzxml'
    default_asc_model = 'models/cnn_normmc/ascending.npz'
    default_desc_model = 'models/cnn_normmc/descending.npz'
    main.main(audio_file_path, default_asc_model, default_desc_model, output_dir)

    # synthesize mzxml
    pass

@socketio.on('disconnect')
def test_disconnect():
    emit('disconnected', {'status': 'disconnected'})



if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')