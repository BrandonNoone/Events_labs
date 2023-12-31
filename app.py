from flask import Flask
from controller.events_controller import events_blueprint

app = Flask(__name__)
app.register_blueprint(events_blueprint)

@app.route("/")
def hello_world():
    return "<h1>Hello world</1>"

