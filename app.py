from flask import Flask, render_template, request, send_from_directory, send_file
from pytube import YouTube

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():

    ret = request.form

    if request.method == 'POST':
        print("Downlaod requested")
        url = ret['URL']
        yt = YouTube(url)

        print("Starting Download ...")
        audio = yt.streams.filter(only_audio=True).first()

        try:
            audio.download('./downloads', filename='song.mp3')
        except Exception:
            print("Downlaod Failed")
            print(Exception.__str__)
        
        print("Downlaod Complete")
        
        return send_file('./downloads/song.mp3', as_attachment=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
