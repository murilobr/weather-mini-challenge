import os

from flask import Flask

from weather.use_cases.retrieve_weather import retrieve_weather_controller

template_dir = os.path.abspath("./weather/templates")
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def index():
    return retrieve_weather_controller.handler()
    # return 'Hello, World!'
