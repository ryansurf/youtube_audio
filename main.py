import yt2 as yt
from flask import Flask, render_template, request, send_file
import os


app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/download', methods = ["GET", "POST"])
def download_audio():
    if request.method == "POST":
        try:
            link = request.form.get("linkAudio")
            filename = yt.get_mp3(link)
            title = filename[1]
            result = send_file(filename[0], download_name = title+'.mp3', as_attachment=True) #render_template("index.html", download = True)
            os.remove(filename[0])
            return result
            #return render_template("index.html", download = True)
        except FileNotFoundError:
            return render_template("error.html")

@app.route('/downloadVideo', methods = ["GET", "POST"])
def download_video():
    if request.method == "POST":
        try:
            link = request.form.get("linkVideo")
            filename = yt.get_video(link)
            title = filename[1]
            result = send_file(filename[0], download_name = title+'.mp4', as_attachment=True)
            os.remove(filename[0])
            return result
        except FileNotFoundError:
            pass
            #return render_template("error.html")

    


if __name__ == "__main__":
    app.run()





