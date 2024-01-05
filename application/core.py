from flask import Flask, render_template
from application.config import config

app = Flask(__name__, template_folder="../resources/views")
app.secret_key = config["key"]
app.config['SECRET_KEY'] = config["key"]
