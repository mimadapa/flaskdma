from flask import Flask

app = Flask(__name__)

@app.route("/")
def prueba():
    return "<p>¡prueba!</p>"