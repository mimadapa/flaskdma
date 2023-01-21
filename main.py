from flask import Flask
import imageprocessing as img
app = Flask(__name__)

@app.route("/")
def mail():
    return img.process()