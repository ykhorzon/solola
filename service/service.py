from solola_wrapper.Configuration import Configuration
from solola_wrapper.Solola import Solola
from flask import Flask, escape, request, Response

app = Flask(__name__)

@app.route('/')
def service():
    name = request.args.get("name", "World")
    # TODO: how to define config parameter?
    # config = Configuration({
    #     'audio_fp': '../inputs/test.mp3',
    #     'output_dir': 'output_dir',
    # })
    # solola = Solola(config)
    
    # return f'Hello, {escape(name)}! {solola.transcribe()}'
    return Response("{'a':'b', 'c':'d'}", status=201, mimetype='application/json')


