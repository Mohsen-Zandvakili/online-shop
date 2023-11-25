from flask import Blueprint

app = Blueprint('general', __name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/about")
def about():
    return "Hello, About1"