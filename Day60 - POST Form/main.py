from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    form = request.form
    print(form)
    return render_template("welcome.html", welcome=form)

# @app.route('/welcome')
# def welcome():
#     return render_template("welcome.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)