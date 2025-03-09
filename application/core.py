from flask import Flask, render_template
from application.config import config
from application.constants.paths import APP_PATH

app = Flask(__name__, template_folder=f"{APP_PATH}/resources/views")
app.secret_key = config["key"]
app.config['SECRET_KEY'] = config["key"]
