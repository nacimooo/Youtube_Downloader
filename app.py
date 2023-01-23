from flask import Flask, render_template, request, send_from_directory, send_file
from pytube import YouTube

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    ret = request.form

    if request.method == 'POST':
        url = ret['URL']
        yt = YouTube(url)

        audio = yt.streams.filter(only_audio=True).first()

        audio.download('./downloads', filename='song.mp3')
        return send_file('./downloads/song.mp3', as_attachment=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
