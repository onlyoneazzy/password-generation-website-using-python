from flask import Flask, render_template
from password_generator import password_generator
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/generate_password")
def get_password():
    password = password_generator()

    return render_template(
        "generate_password.html",
        thepassword=password
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)